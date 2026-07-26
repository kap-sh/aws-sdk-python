"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#EncryptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.enabled
    import capo_connectcampaignsv2.types.encryption_key
    import capo_connectcampaignsv2.types.encryption_type


class EncryptionConfig(TypedDict, closed=True):
    enabled: "capo_connectcampaignsv2.types.enabled.Enabled"
    encryption_type: NotRequired[
        "capo_connectcampaignsv2.types.encryption_type.EncryptionType"
    ]
    key_arn: NotRequired["capo_connectcampaignsv2.types.encryption_key.EncryptionKey"]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfig) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "encryption_type" in value:
        out["encryptionType"] = value["encryption_type"]
    if "key_arn" in value:
        out["keyArn"] = value["key_arn"]
    return out


def deserialize_json(data: dict) -> EncryptionConfig:
    out: EncryptionConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "encryptionType" in data:
        out["encryption_type"] = data["encryptionType"]
    if "keyArn" in data:
        out["key_arn"] = data["keyArn"]
    return out
