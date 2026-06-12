"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ValidationExceptionField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.error_message


class ValidationExceptionField(TypedDict):
    name: "str"
    """<p>The name of the field that failed validation.</p>"""
    message: "aws_sdk_mwaa_serverless.types.error_message.ErrorMessage"
    """<p>A message that describes why the field failed validation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
