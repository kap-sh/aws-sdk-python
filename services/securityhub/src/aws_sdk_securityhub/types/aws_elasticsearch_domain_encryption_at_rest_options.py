"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticsearchDomainEncryptionAtRestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsElasticsearchDomainEncryptionAtRestOptions(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether encryption at rest is enabled.</p>"""
    kms_key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The KMS key ID. Takes the form <code>1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticsearchDomainEncryptionAtRestOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> AwsElasticsearchDomainEncryptionAtRestOptions:
    out: AwsElasticsearchDomainEncryptionAtRestOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
