"""Generated from Smithy shape ``com.amazonaws.omics#SseConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.encryption_type


class SseConfig(TypedDict):
    type: "aws_sdk_omics.types.encryption_type.EncryptionType"
    """<p>The encryption type.</p>"""
    key_arn: NotRequired["str"]
    """<p>An encryption key ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SseConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "key_arn" in value:
        out["keyArn"] = value["key_arn"]
    return out


def deserialize_json(data: dict) -> SseConfig:
    out: SseConfig = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SseConfig.type required")
    if "keyArn" in data:
        out["key_arn"] = data["keyArn"]
    return out
