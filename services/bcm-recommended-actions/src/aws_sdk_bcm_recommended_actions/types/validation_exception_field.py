"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#ValidationExceptionField``."""

from typing_extensions import TypedDict

from aws_sdk_bcm_recommended_actions.errors import DeserializationError


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>Provides the name of the field that failed validation.</p>"""
    message: "str"
    """<p>Provides a message explaining why the field failed validation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
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
