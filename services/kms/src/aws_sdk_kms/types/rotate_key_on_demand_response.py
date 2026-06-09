"""Generated from Smithy shape ``com.amazonaws.kms#RotateKeyOnDemandResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_id_type


class RotateKeyOnDemandResponse(TypedDict):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>Identifies the symmetric encryption KMS key that you initiated on-demand rotation on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotateKeyOnDemandResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RotateKeyOnDemandResponse:
    out: RotateKeyOnDemandResponse = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    return out
