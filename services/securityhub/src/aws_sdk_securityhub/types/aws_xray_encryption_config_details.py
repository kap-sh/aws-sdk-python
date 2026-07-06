"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsXrayEncryptionConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsXrayEncryptionConfigDetails(TypedDict, closed=True):
    key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the KMS key that is used for encryption. Provided if <code>Type</code> is <code>KMS</code>.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current status of the encryption configuration. Valid values are <code>ACTIVE</code> or <code>UPDATING</code>.</p> <p>When <code>Status</code> is equal to <code>UPDATING</code>, X-Ray might use both the old and new encryption.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of encryption. <code>KMS</code> indicates that the encryption uses KMS keys. <code>NONE</code> indicates the default encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsXrayEncryptionConfigDetails) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "status" in value:
        out["Status"] = value["status"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsXrayEncryptionConfigDetails:
    out: AwsXrayEncryptionConfigDetails = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
