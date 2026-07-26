"""Generated from Smithy shape ``com.amazonaws.datazone#RowFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.row_filter_expression
    import capo_datazone.types.row_filter_list


class _RowFilter_expression(TypedDict, closed=True):
    expression: "capo_datazone.types.row_filter_expression.RowFilterExpression"


_RowFilter_and = TypedDict(
    "_RowFilter_and",
    {
        "and": "capo_datazone.types.row_filter_list.RowFilterList",
    },
    closed=True,
)


_RowFilter_or = TypedDict(
    "_RowFilter_or",
    {
        "or": "capo_datazone.types.row_filter_list.RowFilterList",
    },
    closed=True,
)

RowFilter: TypeAlias = _RowFilter_expression | _RowFilter_and | _RowFilter_or


# --- restJson1 ser/de ---
def serialize_json(value: RowFilter) -> dict:
    if "expression" in value:
        import capo_datazone.types.row_filter_expression

        return {
            "expression": capo_datazone.types.row_filter_expression.serialize_json(
                value["expression"]
            )
        }
    elif "and" in value:
        import capo_datazone.types.row_filter_list

        return {"and": capo_datazone.types.row_filter_list.serialize_json(value["and"])}
    elif "or" in value:
        import capo_datazone.types.row_filter_list

        return {"or": capo_datazone.types.row_filter_list.serialize_json(value["or"])}
    else:
        raise SerializationError("RowFilter: no variant present")


def deserialize_json(data: dict) -> RowFilter:
    if "expression" in data:
        import capo_datazone.types.row_filter_expression

        return {
            "expression": capo_datazone.types.row_filter_expression.deserialize_json(
                data["expression"]
            )
        }
    elif "and" in data:
        import capo_datazone.types.row_filter_list

        return {
            "and": capo_datazone.types.row_filter_list.deserialize_json(data["and"])
        }
    elif "or" in data:
        import capo_datazone.types.row_filter_list

        return {"or": capo_datazone.types.row_filter_list.deserialize_json(data["or"])}
    else:
        raise DeserializationError("RowFilter: no recognized variant key")
