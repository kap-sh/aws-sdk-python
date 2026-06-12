"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MsSmoothEncryptionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.speke_key_provider


class MsSmoothEncryptionSettings(TypedDict):
    speke_key_provider: NotRequired[
        "aws_sdk_mediaconvert.types.speke_key_provider.SpekeKeyProvider"
    ]
    """If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead."""


# --- restJson1 ser/de ---
def serialize_json(value: MsSmoothEncryptionSettings) -> dict:
    out: dict = {}
    if "speke_key_provider" in value:
        import aws_sdk_mediaconvert.types.speke_key_provider

        out["spekeKeyProvider"] = (
            aws_sdk_mediaconvert.types.speke_key_provider.serialize_json(
                value["speke_key_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> MsSmoothEncryptionSettings:
    out: MsSmoothEncryptionSettings = {}  # type: ignore[typeddict-item]
    if "spekeKeyProvider" in data:
        import aws_sdk_mediaconvert.types.speke_key_provider

        out["speke_key_provider"] = (
            aws_sdk_mediaconvert.types.speke_key_provider.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    return out
