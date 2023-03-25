def log(message):
    with open('log.txt', 'w') as f:
        f.write(message)

log("Test 1")