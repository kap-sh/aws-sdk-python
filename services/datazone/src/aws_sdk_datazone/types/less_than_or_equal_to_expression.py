"""Generated from Smithy shape ``com.amazonaws.datazone#LessThanOrEqualToExpression``."""

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError


class LessThanOrEqualToExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""
    value: "str"
    """<p>The value that might be less than or equal to an expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LessThanOrEqualToExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> LessThanOrEqualToExpression:
    out: LessThanOrEqualToExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("LessThanOrEqualToExpression.column_name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("LessThanOrEqualToExpression.value required")
    return out
