"""Generated from Smithy shape ``com.amazonaws.datazone#GreaterThanOrEqualToExpression``."""

from typing import TypedDict

from aws_sdk_datazone.errors import DeserializationError


class GreaterThanOrEqualToExpression(TypedDict):
    column_name: "str"
    """<p>The name of the column.</p>"""
    value: "str"
    """<p>The value that might be greater than or equal to an expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GreaterThanOrEqualToExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> GreaterThanOrEqualToExpression:
    out: GreaterThanOrEqualToExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError(
            "GreaterThanOrEqualToExpression.column_name required"
        )
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("GreaterThanOrEqualToExpression.value required")
    return out
