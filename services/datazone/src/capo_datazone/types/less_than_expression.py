"""Generated from Smithy shape ``com.amazonaws.datazone#LessThanExpression``."""

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError


class LessThanExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""
    value: "str"
    """<p>The value that might be less than the expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LessThanExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> LessThanExpression:
    out: LessThanExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("LessThanExpression.column_name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("LessThanExpression.value required")
    return out
