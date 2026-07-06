"""Generated from Smithy shape ``com.amazonaws.voiceid#ServerSideEncryptionUpdateDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.kms_key_id
    import aws_sdk_voice_id.types.server_side_encryption_update_status
    import aws_sdk_voice_id.types.string


class ServerSideEncryptionUpdateDetails(TypedDict, closed=True):
    old_kms_key_id: NotRequired["aws_sdk_voice_id.types.kms_key_id.KmsKeyId"]
    """<p>The previous KMS key ID the domain was encrypted with, before ServerSideEncryptionConfiguration was updated to a new KMS key ID.</p>"""
    update_status: NotRequired[
        "aws_sdk_voice_id.types.server_side_encryption_update_status.ServerSideEncryptionUpdateStatus"
    ]
    """<p>Status of the server-side encryption update. During an update, if there is an issue with the domain's current or old KMS key ID, such as an inaccessible or disabled key, then the status is FAILED. In order to resolve this, the key needs to be made accessible, and then an UpdateDomain call with the existing server-side encryption configuration will re-attempt this update process.</p>"""
    message: NotRequired["aws_sdk_voice_id.types.string.String"]
    """<p>Message explaining the current UpdateStatus. When the UpdateStatus is FAILED, this message explains the cause of the failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServerSideEncryptionUpdateDetails) -> dict:
    out: dict = {}
    if "old_kms_key_id" in value:
        out["OldKmsKeyId"] = value["old_kms_key_id"]
    if "update_status" in value:
        out["UpdateStatus"] = value["update_status"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServerSideEncryptionUpdateDetails:
    out: ServerSideEncryptionUpdateDetails = {}  # type: ignore[typeddict-item]
    if "OldKmsKeyId" in data:
        out["old_kms_key_id"] = data["OldKmsKeyId"]
    if "UpdateStatus" in data:
        out["update_status"] = data["UpdateStatus"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
