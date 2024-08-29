import markov

if __name__ == '__main__':
    chain = markov.MarkovChain()
    chain.train(markov.text)
    sample_prompt = "He was suddenly"
    # pick the last word and generate a new word relying on exiting text
    # repeat the auto-completion here 15 times and each time append the
    # newly picked word at the tail of the original text
    result = chain.generate(sample_prompt, 15)

    print(result)
