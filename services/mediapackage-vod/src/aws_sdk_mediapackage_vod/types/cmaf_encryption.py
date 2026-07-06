"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#CmafEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.speke_key_provider


class CmafEncryption(TypedDict, closed=True):
    constant_initialization_vector: NotRequired[
        "aws_sdk_mediapackage_vod.types.__string.__string"
    ]
    """An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you don't specify a value, then MediaPackage creates the constant initialization vector (IV)."""
    speke_key_provider: NotRequired[
        "aws_sdk_mediapackage_vod.types.speke_key_provider.SpekeKeyProvider"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CmafEncryption) -> dict:
    out: dict = {}
    if "constant_initialization_vector" in value:
        out["constantInitializationVector"] = value["constant_initialization_vector"]
    if "speke_key_provider" in value:
        import aws_sdk_mediapackage_vod.types.speke_key_provider

        out["spekeKeyProvider"] = (
            aws_sdk_mediapackage_vod.types.speke_key_provider.serialize_json(
                value["speke_key_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> CmafEncryption:
    out: CmafEncryption = {}  # type: ignore[typeddict-item]
    if "constantInitializationVector" in data:
        out["constant_initialization_vector"] = data["constantInitializationVector"]
    if "spekeKeyProvider" in data:
        import aws_sdk_mediapackage_vod.types.speke_key_provider

        out["speke_key_provider"] = (
            aws_sdk_mediapackage_vod.types.speke_key_provider.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    return out
