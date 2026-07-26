"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.dolby_vision_compatibility
    import capo_mediaconvert.types.dolby_vision_level6_metadata
    import capo_mediaconvert.types.dolby_vision_level6_mode
    import capo_mediaconvert.types.dolby_vision_mapping
    import capo_mediaconvert.types.dolby_vision_profile


class DolbyVision(TypedDict, closed=True):
    compatibility: NotRequired[
        "capo_mediaconvert.types.dolby_vision_compatibility.DolbyVisionCompatibility"
    ]
    """When you set Compatibility mapping to Duplicate Stream, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause a duplicate stream to be signaled in the manifest as a duplicate stream. When you set Compatibility mapping to Supplemntal Codecs, DolbyVision streams that have a backward compatible base layer (e.g., DolbyVision 8.1) will cause the associate stream in the manifest to include a SUPPLEMENTAL_CODECS property."""
    l6_metadata: NotRequired[
        "capo_mediaconvert.types.dolby_vision_level6_metadata.DolbyVisionLevel6Metadata"
    ]
    """Use these settings when you set DolbyVisionLevel6Mode to SPECIFY to override the MaxCLL and MaxFALL values in your input with new values."""
    l6_mode: NotRequired[
        "capo_mediaconvert.types.dolby_vision_level6_mode.DolbyVisionLevel6Mode"
    ]
    """Use Dolby Vision Mode to choose how the service will handle Dolby Vision MaxCLL and MaxFALL properies."""
    mapping: NotRequired[
        "capo_mediaconvert.types.dolby_vision_mapping.DolbyVisionMapping"
    ]
    """Required when you set Dolby Vision Profile to Profile 8.1. When you set Content mapping to None, content mapping is not applied to the HDR10-compatible signal. Depending on the source peak nit level, clipping might occur on HDR devices without Dolby Vision. When you set Content mapping to HDR10 1000, the transcoder creates a 1,000 nits peak HDR10-compatible signal by applying static content mapping to the source. This mode is speed-optimized for PQ10 sources with metadata that is created from analysis. For graded Dolby Vision content, be aware that creative intent might not be guaranteed with extreme 1,000 nits trims."""
    profile: NotRequired[
        "capo_mediaconvert.types.dolby_vision_profile.DolbyVisionProfile"
    ]
    """Required when you enable Dolby Vision. Use Profile 5 to include frame-interleaved Dolby Vision metadata in your output. Your input must include Dolby Vision metadata or an HDR10 YUV color space. Use Profile 8.1 to include frame-interleaved Dolby Vision metadata and HDR10 metadata in your output. Your input must include Dolby Vision metadata."""


# --- restJson1 ser/de ---
def serialize_json(value: DolbyVision) -> dict:
    out: dict = {}
    if "compatibility" in value:
        import capo_mediaconvert.types.dolby_vision_compatibility

        out["compatibility"] = (
            capo_mediaconvert.types.dolby_vision_compatibility.serialize_json(
                value["compatibility"]
            )
        )
    if "l6_metadata" in value:
        import capo_mediaconvert.types.dolby_vision_level6_metadata

        out["l6Metadata"] = (
            capo_mediaconvert.types.dolby_vision_level6_metadata.serialize_json(
                value["l6_metadata"]
            )
        )
    if "l6_mode" in value:
        import capo_mediaconvert.types.dolby_vision_level6_mode

        out["l6Mode"] = capo_mediaconvert.types.dolby_vision_level6_mode.serialize_json(
            value["l6_mode"]
        )
    if "mapping" in value:
        import capo_mediaconvert.types.dolby_vision_mapping

        out["mapping"] = capo_mediaconvert.types.dolby_vision_mapping.serialize_json(
            value["mapping"]
        )
    if "profile" in value:
        import capo_mediaconvert.types.dolby_vision_profile

        out["profile"] = capo_mediaconvert.types.dolby_vision_profile.serialize_json(
            value["profile"]
        )
    return out


def deserialize_json(data: dict) -> DolbyVision:
    out: DolbyVision = {}  # type: ignore[typeddict-item]
    if "compatibility" in data:
        import capo_mediaconvert.types.dolby_vision_compatibility

        out["compatibility"] = (
            capo_mediaconvert.types.dolby_vision_compatibility.deserialize_json(
                data["compatibility"]
            )
        )
    if "l6Metadata" in data:
        import capo_mediaconvert.types.dolby_vision_level6_metadata

        out["l6_metadata"] = (
            capo_mediaconvert.types.dolby_vision_level6_metadata.deserialize_json(
                data["l6Metadata"]
            )
        )
    if "l6Mode" in data:
        import capo_mediaconvert.types.dolby_vision_level6_mode

        out["l6_mode"] = (
            capo_mediaconvert.types.dolby_vision_level6_mode.deserialize_json(
                data["l6Mode"]
            )
        )
    if "mapping" in data:
        import capo_mediaconvert.types.dolby_vision_mapping

        out["mapping"] = capo_mediaconvert.types.dolby_vision_mapping.deserialize_json(
            data["mapping"]
        )
    if "profile" in data:
        import capo_mediaconvert.types.dolby_vision_profile

        out["profile"] = capo_mediaconvert.types.dolby_vision_profile.deserialize_json(
            data["profile"]
        )
    return out
