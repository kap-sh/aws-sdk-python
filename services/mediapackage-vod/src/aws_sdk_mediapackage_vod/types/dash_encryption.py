"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DashEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.speke_key_provider


class DashEncryption(TypedDict, closed=True):
    speke_key_provider: NotRequired[
        "aws_sdk_mediapackage_vod.types.speke_key_provider.SpekeKeyProvider"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DashEncryption) -> dict:
    out: dict = {}
    if "speke_key_provider" in value:
        import aws_sdk_mediapackage_vod.types.speke_key_provider

        out["spekeKeyProvider"] = (
            aws_sdk_mediapackage_vod.types.speke_key_provider.serialize_json(
                value["speke_key_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashEncryption:
    out: DashEncryption = {}  # type: ignore[typeddict-item]
    if "spekeKeyProvider" in data:
        import aws_sdk_mediapackage_vod.types.speke_key_provider

        out["speke_key_provider"] = (
            aws_sdk_mediapackage_vod.types.speke_key_provider.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    return out
