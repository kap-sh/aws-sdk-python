"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsEncryptionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_min32_max32_pattern09a_faf32
    import aws_sdk_mediaconvert.types.hls_encryption_type
    import aws_sdk_mediaconvert.types.hls_initialization_vector_in_manifest
    import aws_sdk_mediaconvert.types.hls_key_provider_type
    import aws_sdk_mediaconvert.types.hls_offline_encrypted
    import aws_sdk_mediaconvert.types.speke_key_provider
    import aws_sdk_mediaconvert.types.static_key_provider


class HlsEncryptionSettings(TypedDict):
    constant_initialization_vector: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min32_max32_pattern09a_faf32.__stringMin32Max32Pattern09aFAF32"
    ]
    """This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default."""
    encryption_method: NotRequired[
        "aws_sdk_mediaconvert.types.hls_encryption_type.HlsEncryptionType"
    ]
    """Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting 'Disabled' in the web interface also disables encryption."""
    initialization_vector_in_manifest: NotRequired[
        "aws_sdk_mediaconvert.types.hls_initialization_vector_in_manifest.HlsInitializationVectorInManifest"
    ]
    """The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest."""
    offline_encrypted: NotRequired[
        "aws_sdk_mediaconvert.types.hls_offline_encrypted.HlsOfflineEncrypted"
    ]
    """Enable this setting to insert the EXT-X-SESSION-KEY element into the master playlist. This allows for offline Apple HLS FairPlay content protection."""
    speke_key_provider: NotRequired[
        "aws_sdk_mediaconvert.types.speke_key_provider.SpekeKeyProvider"
    ]
    """If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead."""
    static_key_provider: NotRequired[
        "aws_sdk_mediaconvert.types.static_key_provider.StaticKeyProvider"
    ]
    """Use these settings to set up encryption with a static key provider."""
    type: NotRequired[
        "aws_sdk_mediaconvert.types.hls_key_provider_type.HlsKeyProviderType"
    ]
    """Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsEncryptionSettings) -> dict:
    out: dict = {}
    if "constant_initialization_vector" in value:
        out["constantInitializationVector"] = value["constant_initialization_vector"]
    if "encryption_method" in value:
        import aws_sdk_mediaconvert.types.hls_encryption_type

        out["encryptionMethod"] = (
            aws_sdk_mediaconvert.types.hls_encryption_type.serialize_json(
                value["encryption_method"]
            )
        )
    if "initialization_vector_in_manifest" in value:
        import aws_sdk_mediaconvert.types.hls_initialization_vector_in_manifest

        out["initializationVectorInManifest"] = (
            aws_sdk_mediaconvert.types.hls_initialization_vector_in_manifest.serialize_json(
                value["initialization_vector_in_manifest"]
            )
        )
    if "offline_encrypted" in value:
        import aws_sdk_mediaconvert.types.hls_offline_encrypted

        out["offlineEncrypted"] = (
            aws_sdk_mediaconvert.types.hls_offline_encrypted.serialize_json(
                value["offline_encrypted"]
            )
        )
    if "speke_key_provider" in value:
        import aws_sdk_mediaconvert.types.speke_key_provider

        out["spekeKeyProvider"] = (
            aws_sdk_mediaconvert.types.speke_key_provider.serialize_json(
                value["speke_key_provider"]
            )
        )
    if "static_key_provider" in value:
        import aws_sdk_mediaconvert.types.static_key_provider

        out["staticKeyProvider"] = (
            aws_sdk_mediaconvert.types.static_key_provider.serialize_json(
                value["static_key_provider"]
            )
        )
    if "type" in value:
        import aws_sdk_mediaconvert.types.hls_key_provider_type

        out["type"] = aws_sdk_mediaconvert.types.hls_key_provider_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> HlsEncryptionSettings:
    out: HlsEncryptionSettings = {}  # type: ignore[typeddict-item]
    if "constantInitializationVector" in data:
        out["constant_initialization_vector"] = data["constantInitializationVector"]
    if "encryptionMethod" in data:
        import aws_sdk_mediaconvert.types.hls_encryption_type

        out["encryption_method"] = (
            aws_sdk_mediaconvert.types.hls_encryption_type.deserialize_json(
                data["encryptionMethod"]
            )
        )
    if "initializationVectorInManifest" in data:
        import aws_sdk_mediaconvert.types.hls_initialization_vector_in_manifest

        out["initialization_vector_in_manifest"] = (
            aws_sdk_mediaconvert.types.hls_initialization_vector_in_manifest.deserialize_json(
                data["initializationVectorInManifest"]
            )
        )
    if "offlineEncrypted" in data:
        import aws_sdk_mediaconvert.types.hls_offline_encrypted

        out["offline_encrypted"] = (
            aws_sdk_mediaconvert.types.hls_offline_encrypted.deserialize_json(
                data["offlineEncrypted"]
            )
        )
    if "spekeKeyProvider" in data:
        import aws_sdk_mediaconvert.types.speke_key_provider

        out["speke_key_provider"] = (
            aws_sdk_mediaconvert.types.speke_key_provider.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    if "staticKeyProvider" in data:
        import aws_sdk_mediaconvert.types.static_key_provider

        out["static_key_provider"] = (
            aws_sdk_mediaconvert.types.static_key_provider.deserialize_json(
                data["staticKeyProvider"]
            )
        )
    if "type" in data:
        import aws_sdk_mediaconvert.types.hls_key_provider_type

        out["type"] = aws_sdk_mediaconvert.types.hls_key_provider_type.deserialize_json(
            data["type"]
        )
    return out
