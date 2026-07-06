"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether encryption at rest is enabled.</p>"""
    kms_key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The KMS key ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails,
) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(
    data: dict,
) -> AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails:
    out: AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
