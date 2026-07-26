"""Generated from Smithy shape ``com.amazonaws.datazone#NotEqualToExpression``."""

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError


class NotEqualToExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""
    value: "str"
    """<p>The value that might not be equal to the expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotEqualToExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> NotEqualToExpression:
    out: NotEqualToExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("NotEqualToExpression.column_name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("NotEqualToExpression.value required")
    return out
