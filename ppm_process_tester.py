from ppm_process import *


def main():
    # test process
    print("*** testing process ***")
    # TODO: add test cases to thoroughly test this function
    assert process(["255 0 0 0 0 0", "255 255 255 0 0 0"], 3, 4) == [[255, 0, 0, 0], [0, 0, 255, 255], [255, 0, 0, 0]]
    assert process(["255 0 0 0 0 0", "255 255 255 0 0 0"], 1, 12) == [[255, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0]]
    assert type(process(["255 0 0 0 0 0", "255 255 255 0 0 0"], 1, 12)) == list
    assert process([], 3, 4) == [[], [], []]
    assert process(["255 0 0 0 0 0", "255 255 255 0 0 0"], 0, 0) == []
    print("process passed")

    # test scale
    print("*** testing scale ***")
    # TODO: add test cases to thoroughly test this function
    assert type(scale([[255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255]], 3, 2)) == list
    assert scale([], 1, 2) == []
    assert scale([[255, 0, 0, 0, 0, 255], [255, 0, 0, 0, 255, 0]], 2, 3) == [[255, 0, 0]]
    assert scale([[255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 255, 6]], 4, 2) == [[255, 0, 0]]
    assert scale([[255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 255, 6]], 1, 1) == [[255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 255, 6]]
    assert scale([[255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 255, 6]], 10, 10) == [[255, 0, 0]]
    print("scale passed")


if __name__ == "__main__":
    main()