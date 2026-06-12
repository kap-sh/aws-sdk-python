"""Generated from Smithy shape ``com.amazonaws.frauddetector#KMSKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.kms_encryption_key_arn


class KMSKey(TypedDict):
    kms_encryption_key_arn: NotRequired[
        "aws_sdk_frauddetector.types.kms_encryption_key_arn.KmsEncryptionKeyArn"
    ]
    """<p>The encryption key ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSKey) -> dict:
    out: dict = {}
    if "kms_encryption_key_arn" in value:
        out["kmsEncryptionKeyArn"] = value["kms_encryption_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSKey:
    out: KMSKey = {}  # type: ignore[typeddict-item]
    if "kmsEncryptionKeyArn" in data:
        out["kms_encryption_key_arn"] = data["kmsEncryptionKeyArn"]
    return out
