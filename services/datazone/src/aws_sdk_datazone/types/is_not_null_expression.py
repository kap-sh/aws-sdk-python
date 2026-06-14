"""Generated from Smithy shape ``com.amazonaws.datazone#IsNotNullExpression``."""

from typing import TypedDict

from aws_sdk_datazone.errors import DeserializationError


class IsNotNullExpression(TypedDict):
    column_name: "str"
    """<p>The name of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsNotNullExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    return out


def deserialize_json(data: dict) -> IsNotNullExpression:
    out: IsNotNullExpression = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("IsNotNullExpression.column_name required")
    return out
