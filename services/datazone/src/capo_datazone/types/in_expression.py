"""Generated from Smithy shape ``com.amazonaws.datazone#InExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.string_list


class InExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""
    values: "capo_datazone.types.string_list.StringList"
    """<p>The values that might be in the expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    import capo_datazone.types.string_list

    out["values"] = capo_datazone.types.string_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> InExpression:
    out: InExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("InExpression.column_name required")
    if "values" in data:
        import capo_datazone.types.string_list

        out["values"] = capo_datazone.types.string_list.deserialize_json(data["values"])
    else:
        raise DeserializationError("InExpression.values required")
    return out
