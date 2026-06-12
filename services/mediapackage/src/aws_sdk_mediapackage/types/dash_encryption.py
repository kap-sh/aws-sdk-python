"""Generated from Smithy shape ``com.amazonaws.mediapackage#DashEncryption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__integer
    import aws_sdk_mediapackage.types.speke_key_provider


class DashEncryption(TypedDict):
    key_rotation_interval_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Time (in seconds) between each encryption key rotation."""
    speke_key_provider: NotRequired[
        "aws_sdk_mediapackage.types.speke_key_provider.SpekeKeyProvider"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DashEncryption) -> dict:
    out: dict = {}
    if "key_rotation_interval_seconds" in value:
        out["keyRotationIntervalSeconds"] = value["key_rotation_interval_seconds"]
    if "speke_key_provider" in value:
        import aws_sdk_mediapackage.types.speke_key_provider

        out["spekeKeyProvider"] = (
            aws_sdk_mediapackage.types.speke_key_provider.serialize_json(
                value["speke_key_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashEncryption:
    out: DashEncryption = {}  # type: ignore[typeddict-item]
    if "keyRotationIntervalSeconds" in data:
        out["key_rotation_interval_seconds"] = data["keyRotationIntervalSeconds"]
    if "spekeKeyProvider" in data:
        import aws_sdk_mediapackage.types.speke_key_provider

        out["speke_key_provider"] = (
            aws_sdk_mediapackage.types.speke_key_provider.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    return out
