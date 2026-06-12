"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ValidationExceptionField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.validation_exception_error_code


class ValidationExceptionField(TypedDict):
    name: "str"
    """<p>The name of the field that failed validation.</p>"""
    message: "str"
    """<p>A detailed message explaining why the field validation failed.</p>"""
    code: NotRequired[
        "aws_sdk_partnercentral_benefits.types.validation_exception_error_code.ValidationExceptionErrorCode"
    ]
    """<p>An error code explaining why the field validation failed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Message"] = value["message"]
    if "code" in value:
        import aws_sdk_partnercentral_benefits.types.validation_exception_error_code

        out["Code"] = (
            aws_sdk_partnercentral_benefits.types.validation_exception_error_code.serialize_aws_json_1_0(
                value["code"]
            )
        )
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
    if "Code" in data:
        import aws_sdk_partnercentral_benefits.types.validation_exception_error_code

        out["code"] = (
            aws_sdk_partnercentral_benefits.types.validation_exception_error_code.deserialize_aws_json_1_0(
                data["Code"]
            )
        )
    return out
