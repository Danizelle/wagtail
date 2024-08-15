import pytest

class TestgetTextLabel:
    def __init__(self):
        self.children = []

    def getTextLabel(self, opts):
        result = ""
        maxLength = opts.get('maxLength', None)
        for child in self.children:
            childLabel = child.getTextLabel(opts)
            if result:
                newResult = result + ', ' + childLabel
            else:
                newResult = childLabel

            if maxLength is not None and len(newResult) > maxLength - 1:
                if not result.endswith('…'):
                    result += '…'
                break
            else:
                result = newResult
        return result

    # CT1: maxLength permitido é nulo
    @pytest.mark.parametrize("opts, expected_result", [
        ({}, 'child1, child2')  # maxLength é nulo (não especificado)
    ])
    def test_max_length_null(self, opts, expected_result):
        child1 = TestgetTextLabel()
        child1.getTextLabel = lambda opts: 'child1'

        child2 = TestgetTextLabel()
        child2.getTextLabel = lambda opts: 'child2'

        my_obj = TestgetTextLabel()
        my_obj.children = [child1, child2]

        result = my_obj.getTextLabel(opts)

        assert result == expected_result

    # CT2: new Result é menor que comprimento máximo permitido
    @pytest.mark.parametrize("opts, expected_result", [
        ({'maxLength': 100}, 'child1, child2')  # newResult é menor que maxLength - 1
    ])
    def test_new_result_less_than_max_length(self, opts, expected_result):
        pass
