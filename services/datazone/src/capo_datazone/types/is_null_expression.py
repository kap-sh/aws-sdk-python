"""Generated from Smithy shape ``com.amazonaws.datazone#IsNullExpression``."""

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError


class IsNullExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsNullExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    return out


def deserialize_json(data: dict) -> IsNullExpression:
    out: IsNullExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("IsNullExpression.column_name required")
    return out
