"""Generated from Smithy shape ``com.amazonaws.shield#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.string


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_shield.types.string.String"
    """<p>The name of the parameter that failed validation.</p>"""
    message: "capo_shield.types.string.String"
    """<p>The message describing why the parameter failed validation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationExceptionField:
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
