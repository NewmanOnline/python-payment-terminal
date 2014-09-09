import unittest

from nm_payment.drivers.bbs import messages


class TestBBSMessages(unittest.TestCase):
    def test_pack_display_text(self):
        self.assertEqual(
            b'\x41000Hello World',
            messages.pack_display_text("Hello World")
        )

        self.assertEqual(
            b'\x41100Prompt customer',
            messages.pack_display_text("Prompt customer", prompt_customer=True)
        )

        self.assertEqual(
            b'\x41010Expects input',
            messages.pack_display_text("Expects input", expects_input=True)
        )

    def test_unpack_display_text(self):
        message = messages.unpack_display_text(b'\x41000Hello World')
        self.assertFalse(message.prompt_customer)
        self.assertFalse(message.expects_input)
        self.assertEqual(message.text, "Hello World")

        message = messages.unpack_display_text(b'\x41100Prompt customer')
        self.assertTrue(message.prompt_customer)
        self.assertFalse(message.expects_input)
        self.assertEqual(message.text, "Prompt customer")

        message = messages.unpack_display_text(b'\x41010Expects input')
        self.assertFalse(message.prompt_customer)
        self.assertTrue(message.expects_input)
        self.assertEqual(message.text, "Expects input")

    def test_pack_print_text(self):
        self.assertEqual(
            messages.pack_print_text([
                ('write', "First"),
                ('cut-partial'),
                ('write', "Second"),
                ('cut-through'),
            ]),
            b'\x42\x20\x22\x2aFirst\x0eSecond\x0c'
        )

    def test_unpack_print_text(self):
        commands = list(messages.unpack_print_text(
            b'\x42\x20\x22\x2aFirst\x0eSecond\x0c'
        ))
        self.assertEqual(
            commands,
            [
                ('write', "First"),
                ('cut-partial'),
                ('write', "Second"),
                ('cut-through'),
            ]
        )

    def test_pack_reset_timer(self):
        self.assertEqual(messages.pack_reset_timer(60), b'\x43060')

        try:
            messages.pack_reset_timer(6000)
        except ValueError:
            pass
        else:
            self.fail()

    def test_unpack_reset_timer(self):
        self.assertEqual(messages.unpack_reset_timer(b'\x43060'), 60)

        try:
            messages.unpack_reset_timer(b'\x43abc')
        except:
            pass
        else:
            self.fail()