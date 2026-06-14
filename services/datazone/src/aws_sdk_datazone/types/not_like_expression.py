"""Generated from Smithy shape ``com.amazonaws.datazone#NotLikeExpression``."""

from typing import TypedDict

from aws_sdk_datazone.errors import DeserializationError


class NotLikeExpression(TypedDict):
    column_name: "str"
    """<p>The name of the column.</p>"""
    value: "str"
    """<p>The value that might not be like the expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotLikeExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> NotLikeExpression:
    out: NotLikeExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("NotLikeExpression.column_name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("NotLikeExpression.value required")
    return out
