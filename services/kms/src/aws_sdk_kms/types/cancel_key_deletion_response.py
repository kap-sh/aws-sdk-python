"""Generated from Smithy shape ``com.amazonaws.kms#CancelKeyDeletionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_id_type


class CancelKeyDeletionResponse(TypedDict):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key whose deletion is canceled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelKeyDeletionResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelKeyDeletionResponse:
    out: CancelKeyDeletionResponse = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    return out
