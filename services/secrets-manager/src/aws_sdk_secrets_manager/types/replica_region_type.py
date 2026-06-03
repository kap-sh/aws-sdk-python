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
