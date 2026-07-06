"""Generated from Smithy shape ``com.amazonaws.medialive#AccountConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class AccountConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specifies the KMS key to use for all features that use key encryption. Specify the ARN of a KMS key that you have created. Or leave blank to use the key that MediaLive creates and manages for you."""


# --- restJson1 ser/de ---
def serialize_json(value: AccountConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> AccountConfiguration:
    out: AccountConfiguration = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
