"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteGrantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.status_reason_message
    import aws_sdk_license_manager.types.string


class DeleteGrantRequest(TypedDict):
    grant_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the grant.</p>"""
    status_reason: NotRequired[
        "aws_sdk_license_manager.types.status_reason_message.StatusReasonMessage"
    ]
    """<p>The Status reason for the delete request.</p>"""
    version: "aws_sdk_license_manager.types.string.String"
    """<p>Current version of the grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGrantRequest) -> dict:
    out: dict = {}
    out["GrantArn"] = value["grant_arn"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGrantRequest:
    out: DeleteGrantRequest = {}  # type: ignore[typeddict-item]
    if "GrantArn" in data:
        out["grant_arn"] = data["GrantArn"]
    else:
        raise DeserializationError("DeleteGrantRequest.grant_arn required")
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("DeleteGrantRequest.version required")
    return out
