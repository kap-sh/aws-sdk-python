"""Generated from Smithy shape ``com.amazonaws.datazone#GreaterThanExpression``."""

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError


class GreaterThanExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""
    value: "str"
    """<p>The value that might be greater than an expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GreaterThanExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> GreaterThanExpression:
    out: GreaterThanExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("GreaterThanExpression.column_name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("GreaterThanExpression.value required")
    return out
