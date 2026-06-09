"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidationErrorsEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_message
    import aws_sdk_secrets_manager.types.name_type


class ValidationErrorsEntry(TypedDict):
    check_name: NotRequired["aws_sdk_secrets_manager.types.name_type.NameType"]
    """<p>Checks the name of the policy.</p>"""
    error_message: NotRequired[
        "aws_sdk_secrets_manager.types.error_message.ErrorMessage"
    ]
    """<p>Displays error messages if validation encounters problems during validation of the resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationErrorsEntry) -> dict:
    out: dict = {}
    if "check_name" in value:
        out["CheckName"] = value["check_name"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationErrorsEntry:
    out: ValidationErrorsEntry = {}  # type: ignore[typeddict-item]
    if "CheckName" in data:
        out["check_name"] = data["CheckName"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
