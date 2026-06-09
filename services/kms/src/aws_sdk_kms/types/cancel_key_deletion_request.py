"""Generated from Smithy shape ``com.amazonaws.kms#CancelKeyDeletionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_id_type


class CancelKeyDeletionRequest(TypedDict):
    key_id: "aws_sdk_kms.types.key_id_type.KeyIdType"
    """<p>Identifies the KMS key whose deletion is being canceled.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelKeyDeletionRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelKeyDeletionRequest:
    out: CancelKeyDeletionRequest = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("CancelKeyDeletionRequest.key_id required")
    return out
