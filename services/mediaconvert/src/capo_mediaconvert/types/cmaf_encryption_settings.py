"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafEncryptionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max9999
    import capo_mediaconvert.types.__string_min32_max32_pattern09a_faf32
    import capo_mediaconvert.types.cmaf_encryption_type
    import capo_mediaconvert.types.cmaf_initialization_vector_in_manifest
    import capo_mediaconvert.types.cmaf_key_provider_type
    import capo_mediaconvert.types.speke_key_provider_cmaf
    import capo_mediaconvert.types.static_key_provider


class CmafEncryptionSettings(TypedDict, closed=True):
    clear_lead_segments: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max9999.__integerMin1Max9999"
    ]
    """Reduce video startup latency by leaving initial segments unencrypted while DRM license retrieval occurs in parallel. This optimization allows immediate playback startup while maintaining content protection for the remainder of the stream. Specify the number of initial segments to leave unencrypted. Omit this field to disable Clear Lead. The HLS manifest will omit #EXT-X-KEY tags during clear segments and insert the first #EXT-X-KEY immediately before the first encrypted segment. Because encryption is applied at the fragment level, the actual duration of unencrypted content may be slightly longer than expected if the segment length is not evenly divisible by the fragment length. In such cases, encryption begins at the next fragment boundary after the specified clear lead segments, rather than at the exact segment boundary. This feature is supported exclusively for CMAF HLS (fMP4) outputs and is compatible with all existing key provider integrations (SPEKE v1, SPEKE v2, and Static Key encryption). Supported codecs: H.264, H.265, and AV1 video codecs, and AAC audio codec."""
    constant_initialization_vector: NotRequired[
        "capo_mediaconvert.types.__string_min32_max32_pattern09a_faf32.__stringMin32Max32Pattern09aFAF32"
    ]
    """This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default."""
    encryption_method: NotRequired[
        "capo_mediaconvert.types.cmaf_encryption_type.CmafEncryptionType"
    ]
    """Specify the encryption scheme that you want the service to use when encrypting your CMAF segments. Choose AES-CBC subsample or AES_CTR."""
    initialization_vector_in_manifest: NotRequired[
        "capo_mediaconvert.types.cmaf_initialization_vector_in_manifest.CmafInitializationVectorInManifest"
    ]
    """When you use DRM with CMAF outputs, choose whether the service writes the 128-bit encryption initialization vector in the HLS and DASH manifests."""
    speke_key_provider: NotRequired[
        "capo_mediaconvert.types.speke_key_provider_cmaf.SpekeKeyProviderCmaf"
    ]
    """If your output group type is CMAF, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is HLS, DASH, or Microsoft Smooth, use the SpekeKeyProvider settings instead."""
    static_key_provider: NotRequired[
        "capo_mediaconvert.types.static_key_provider.StaticKeyProvider"
    ]
    """Use these settings to set up encryption with a static key provider."""
    type: NotRequired[
        "capo_mediaconvert.types.cmaf_key_provider_type.CmafKeyProviderType"
    ]
    """Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html."""


# --- restJson1 ser/de ---
def serialize_json(value: CmafEncryptionSettings) -> dict:
    out: dict = {}
    if "clear_lead_segments" in value:
        out["clearLeadSegments"] = value["clear_lead_segments"]
    if "constant_initialization_vector" in value:
        out["constantInitializationVector"] = value["constant_initialization_vector"]
    if "encryption_method" in value:
        import capo_mediaconvert.types.cmaf_encryption_type

        out["encryptionMethod"] = (
            capo_mediaconvert.types.cmaf_encryption_type.serialize_json(
                value["encryption_method"]
            )
        )
    if "initialization_vector_in_manifest" in value:
        import capo_mediaconvert.types.cmaf_initialization_vector_in_manifest

        out["initializationVectorInManifest"] = (
            capo_mediaconvert.types.cmaf_initialization_vector_in_manifest.serialize_json(
                value["initialization_vector_in_manifest"]
            )
        )
    if "speke_key_provider" in value:
        import capo_mediaconvert.types.speke_key_provider_cmaf

        out["spekeKeyProvider"] = (
            capo_mediaconvert.types.speke_key_provider_cmaf.serialize_json(
                value["speke_key_provider"]
            )
        )
    if "static_key_provider" in value:
        import capo_mediaconvert.types.static_key_provider

        out["staticKeyProvider"] = (
            capo_mediaconvert.types.static_key_provider.serialize_json(
                value["static_key_provider"]
            )
        )
    if "type" in value:
        import capo_mediaconvert.types.cmaf_key_provider_type

        out["type"] = capo_mediaconvert.types.cmaf_key_provider_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> CmafEncryptionSettings:
    out: CmafEncryptionSettings = {}  # type: ignore[typeddict-item]
    if "clearLeadSegments" in data:
        out["clear_lead_segments"] = data["clearLeadSegments"]
    if "constantInitializationVector" in data:
        out["constant_initialization_vector"] = data["constantInitializationVector"]
    if "encryptionMethod" in data:
        import capo_mediaconvert.types.cmaf_encryption_type

        out["encryption_method"] = (
            capo_mediaconvert.types.cmaf_encryption_type.deserialize_json(
                data["encryptionMethod"]
            )
        )
    if "initializationVectorInManifest" in data:
        import capo_mediaconvert.types.cmaf_initialization_vector_in_manifest

        out["initialization_vector_in_manifest"] = (
            capo_mediaconvert.types.cmaf_initialization_vector_in_manifest.deserialize_json(
                data["initializationVectorInManifest"]
            )
        )
    if "spekeKeyProvider" in data:
        import capo_mediaconvert.types.speke_key_provider_cmaf

        out["speke_key_provider"] = (
            capo_mediaconvert.types.speke_key_provider_cmaf.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    if "staticKeyProvider" in data:
        import capo_mediaconvert.types.static_key_provider

        out["static_key_provider"] = (
            capo_mediaconvert.types.static_key_provider.deserialize_json(
                data["staticKeyProvider"]
            )
        )
    if "type" in data:
        import capo_mediaconvert.types.cmaf_key_provider_type

        out["type"] = capo_mediaconvert.types.cmaf_key_provider_type.deserialize_json(
            data["type"]
        )
    return out
