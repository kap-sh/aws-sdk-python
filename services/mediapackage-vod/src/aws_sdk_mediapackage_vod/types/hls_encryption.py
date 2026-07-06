"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#HlsEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.encryption_method
    import aws_sdk_mediapackage_vod.types.speke_key_provider


class HlsEncryption(TypedDict, closed=True):
    constant_initialization_vector: NotRequired[
        "aws_sdk_mediapackage_vod.types.__string.__string"
    ]
    """A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated."""
    encryption_method: NotRequired[
        "aws_sdk_mediapackage_vod.types.encryption_method.EncryptionMethod"
    ]
    """The encryption method to use."""
    speke_key_provider: NotRequired[
        "aws_sdk_mediapackage_vod.types.speke_key_provider.SpekeKeyProvider"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: HlsEncryption) -> dict:
    out: dict = {}
    if "constant_initialization_vector" in value:
        out["constantInitializationVector"] = value["constant_initialization_vector"]
    if "encryption_method" in value:
        import aws_sdk_mediapackage_vod.types.encryption_method

        out["encryptionMethod"] = (
            aws_sdk_mediapackage_vod.types.encryption_method.serialize_json(
                value["encryption_method"]
            )
        )
    if "speke_key_provider" in value:
        import aws_sdk_mediapackage_vod.types.speke_key_provider

        out["spekeKeyProvider"] = (
            aws_sdk_mediapackage_vod.types.speke_key_provider.serialize_json(
                value["speke_key_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> HlsEncryption:
    out: HlsEncryption = {}  # type: ignore[typeddict-item]
    if "constantInitializationVector" in data:
        out["constant_initialization_vector"] = data["constantInitializationVector"]
    if "encryptionMethod" in data:
        import aws_sdk_mediapackage_vod.types.encryption_method

        out["encryption_method"] = (
            aws_sdk_mediapackage_vod.types.encryption_method.deserialize_json(
                data["encryptionMethod"]
            )
        )
    if "spekeKeyProvider" in data:
        import aws_sdk_mediapackage_vod.types.speke_key_provider

        out["speke_key_provider"] = (
            aws_sdk_mediapackage_vod.types.speke_key_provider.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    return out
