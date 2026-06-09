"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicaRegionType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.kms_key_id_type
    import aws_sdk_secrets_manager.types.region_type


class ReplicaRegionType(TypedDict):
    region: NotRequired["aws_sdk_secrets_manager.types.region_type.RegionType"]
    """<p>A Region code. For a list of Region codes, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints\">Name and code of Regions</a>.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_secrets_manager.types.kms_key_id_type.KmsKeyIdType"
    ]
    """<p>The ARN, key ID, or alias of the KMS key to encrypt the secret. If you don't include this field, Secrets Manager uses <code>aws/secretsmanager</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicaRegionType) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicaRegionType:
    out: ReplicaRegionType = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
