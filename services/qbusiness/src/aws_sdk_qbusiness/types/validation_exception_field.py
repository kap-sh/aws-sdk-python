"""Generated from Smithy shape ``com.amazonaws.qbusiness#ValidationExceptionField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.string


class ValidationExceptionField(TypedDict):
    name: "aws_sdk_qbusiness.types.string.String"
    """<p>The field name where the invalid entry was detected.</p>"""
    message: "aws_sdk_qbusiness.types.string.String"
    """<p>A message about the validation exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
