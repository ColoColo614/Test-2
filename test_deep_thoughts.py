import unittest
from unittest.mock import patch

from deep_thoughts import (
    ACTIONS,
    CLOSERS,
    OPENERS,
    SUBJECTS,
    TWISTS,
    get_random_thought,
    get_total_possible_thoughts,
)


class DeepThoughtTests(unittest.TestCase):
    def test_has_at_least_one_thousand_possible_thoughts(self):
        self.assertGreaterEqual(get_total_possible_thoughts(), 1000)

    def test_uses_all_building_blocks(self):
        with patch("deep_thoughts.random.choice", side_effect=["If", "a coffee mug", "ran a startup", "it would ghost me on Monday mornings", "which proves the universe loves a punchline."]):
            thought = get_random_thought()
        self.assertIn("If", thought)
        self.assertIn("a coffee mug", thought)
        self.assertIn("ran a startup", thought)

    def test_choice_inputs_match_source_lists(self):
        captured = []

        def fake_choice(options):
            captured.append(options)
            return options[0]

        with patch("deep_thoughts.random.choice", side_effect=fake_choice):
            get_random_thought()

        self.assertEqual(captured, [OPENERS, SUBJECTS, ACTIONS, TWISTS, CLOSERS])


if __name__ == "__main__":
    unittest.main()
