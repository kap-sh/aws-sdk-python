"""Generated from Smithy shape ``com.amazonaws.iot#PresignedUrlConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.expires_in_sec
    import aws_sdk_iot.types.role_arn


class PresignedUrlConfig(TypedDict):
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The ARN of an IAM role that grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.</p> <important> <p>For information about addressing the confused deputy problem, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/cross-service-confused-deputy-prevention.html\">cross-service confused deputy prevention</a> in the <i>Amazon Web Services IoT Core developer guide</i>.</p> </important>"""
    expires_in_sec: NotRequired["aws_sdk_iot.types.expires_in_sec.ExpiresInSec"]
    """<p>How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PresignedUrlConfig) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "expires_in_sec" in value:
        out["expiresInSec"] = value["expires_in_sec"]
    return out


def deserialize_json(data: dict) -> PresignedUrlConfig:
    out: PresignedUrlConfig = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "expiresInSec" in data:
        out["expires_in_sec"] = data["expiresInSec"]
    return out
