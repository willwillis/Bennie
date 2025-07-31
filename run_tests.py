from bennie import find_dangling_prepositions

if __name__ == "__main__":
    test_texts = [
        "What are you looking at?",
        "This is the house that Jack built.",
        "To whom did you give the book?",
        "He knew what she was talking about.",
        "I need a pen to write with.",
        "We have something to look forward to.",
        "Where are you going?",
        "She ran into the wall.",
        "He got out.",
        "He got out of the house.",
        "The person I spoke to called me back."
    ]

    print("--- Testing Bennie's Dangling Preposition Detector ---")
    for i, text in enumerate(test_texts):
        print(f"\nTest Case {i+1}: \"{text}\"")
        found, detected_sentences = find_dangling_prepositions(text)
        if found:
            print(f"  Dangling preposition(s) detected in the following sentences:")
            for s in detected_sentences:
                print(f"    - '{s}'")
        else:
            print("  No dangling prepositions detected.")

    print("\n--- End of Tests ---")