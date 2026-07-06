"""Generated from Smithy shape ``com.amazonaws.datazone#EqualToExpression``."""

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError


class EqualToExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""
    value: "str"
    """<p>The value that might be equal to an expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EqualToExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EqualToExpression:
    out: EqualToExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("EqualToExpression.column_name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("EqualToExpression.value required")
    return out
