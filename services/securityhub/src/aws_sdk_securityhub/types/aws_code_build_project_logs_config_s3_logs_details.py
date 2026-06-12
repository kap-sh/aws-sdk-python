"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectLogsConfigS3LogsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsCodeBuildProjectLogsConfigS3LogsDetails(TypedDict):
    encryption_disabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to disable encryption of the S3 build log output.</p>"""
    location: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the S3 bucket and the path prefix for S3 logs.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current status of the S3 build logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectLogsConfigS3LogsDetails) -> dict:
    out: dict = {}
    if "encryption_disabled" in value:
        out["EncryptionDisabled"] = value["encryption_disabled"]
    if "location" in value:
        out["Location"] = value["location"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectLogsConfigS3LogsDetails:
    out: AwsCodeBuildProjectLogsConfigS3LogsDetails = {}  # type: ignore[typeddict-item]
    if "EncryptionDisabled" in data:
        out["encryption_disabled"] = data["EncryptionDisabled"]
    if "Location" in data:
        out["location"] = data["Location"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
