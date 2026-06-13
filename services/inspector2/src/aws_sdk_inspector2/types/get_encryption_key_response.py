"""Generated from Smithy shape ``com.amazonaws.inspector2#GetEncryptionKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.kms_key_arn


class GetEncryptionKeyResponse(TypedDict):
    kms_key_id: "aws_sdk_inspector2.types.kms_key_arn.KmsKeyArn"
    """<p>A kms key ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEncryptionKeyResponse) -> dict:
    out: dict = {}
    out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> GetEncryptionKeyResponse:
    out: GetEncryptionKeyResponse = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        raise DeserializationError("GetEncryptionKeyResponse.kms_key_id required")
    return out
