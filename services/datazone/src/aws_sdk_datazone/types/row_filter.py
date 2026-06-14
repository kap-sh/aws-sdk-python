"""Generated from Smithy shape ``com.amazonaws.datazone#RowFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.row_filter_expression
    import aws_sdk_datazone.types.row_filter_list


class _RowFilter_expression(TypedDict):
    expression: "aws_sdk_datazone.types.row_filter_expression.RowFilterExpression"


_RowFilter_and = TypedDict(
    "_RowFilter_and",
    {
        "and": "aws_sdk_datazone.types.row_filter_list.RowFilterList",
    },
)


_RowFilter_or = TypedDict(
    "_RowFilter_or",
    {
        "or": "aws_sdk_datazone.types.row_filter_list.RowFilterList",
    },
)

RowFilter: TypeAlias = _RowFilter_expression | _RowFilter_and | _RowFilter_or


# --- restJson1 ser/de ---
def serialize_json(value: RowFilter) -> dict:
    if "expression" in value:
        import aws_sdk_datazone.types.row_filter_expression

        return {
            "expression": aws_sdk_datazone.types.row_filter_expression.serialize_json(
                value["expression"]
            )
        }
    elif "and" in value:
        import aws_sdk_datazone.types.row_filter_list

        return {
            "and": aws_sdk_datazone.types.row_filter_list.serialize_json(value["and"])
        }
    elif "or" in value:
        import aws_sdk_datazone.types.row_filter_list

        return {
            "or": aws_sdk_datazone.types.row_filter_list.serialize_json(value["or"])
        }
    else:
        raise SerializationError("RowFilter: no variant present")


def deserialize_json(data: dict) -> RowFilter:
    if "expression" in data:
        import aws_sdk_datazone.types.row_filter_expression

        return {
            "expression": aws_sdk_datazone.types.row_filter_expression.deserialize_json(
                data["expression"]
            )
        }
    elif "and" in data:
        import aws_sdk_datazone.types.row_filter_list

        return {
            "and": aws_sdk_datazone.types.row_filter_list.deserialize_json(data["and"])
        }
    elif "or" in data:
        import aws_sdk_datazone.types.row_filter_list

        return {
            "or": aws_sdk_datazone.types.row_filter_list.deserialize_json(data["or"])
        }
    else:
        raise DeserializationError("RowFilter: no recognized variant key")
