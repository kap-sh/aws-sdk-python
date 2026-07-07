"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.sort_order
    import aws_sdk_lex_models_v2.types.test_execution_sort_attribute


class TestExecutionSortBy(TypedDict, closed=True):
    attribute: "aws_sdk_lex_models_v2.types.test_execution_sort_attribute.TestExecutionSortAttribute"
    """<p>Specifies whether to sort the test set executions by the date and time at which the test sets were created.</p>"""
    order: "aws_sdk_lex_models_v2.types.sort_order.SortOrder"
    """<p>Specifies whether to sort in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionSortBy) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.test_execution_sort_attribute

    out["attribute"] = (
        aws_sdk_lex_models_v2.types.test_execution_sort_attribute.serialize_json(
            value["attribute"]
        )
    )
    import aws_sdk_lex_models_v2.types.sort_order

    out["order"] = aws_sdk_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> TestExecutionSortBy:
    out: TestExecutionSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import aws_sdk_lex_models_v2.types.test_execution_sort_attribute

        out["attribute"] = (
            aws_sdk_lex_models_v2.types.test_execution_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("TestExecutionSortBy.attribute required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.sort_order

        out["order"] = aws_sdk_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("TestExecutionSortBy.order required")
    return out
