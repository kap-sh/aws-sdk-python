"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac3Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max31
    import capo_mediaconvert.types.__integer_min48000_max48000
    import capo_mediaconvert.types.__integer_min64000_max640000
    import capo_mediaconvert.types.ac3_bitstream_mode
    import capo_mediaconvert.types.ac3_coding_mode
    import capo_mediaconvert.types.ac3_dynamic_range_compression_line
    import capo_mediaconvert.types.ac3_dynamic_range_compression_profile
    import capo_mediaconvert.types.ac3_dynamic_range_compression_rf
    import capo_mediaconvert.types.ac3_lfe_filter
    import capo_mediaconvert.types.ac3_metadata_control


class Ac3Settings(TypedDict, closed=True):
    bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min64000_max640000.__integerMin64000Max640000"
    ]
    """Specify the average bitrate in bits per second. The bitrate that you specify must be a multiple of 8000 within the allowed minimum and maximum values. Leave blank to use the default bitrate for the coding mode you select according ETSI TS 102 366. Valid bitrates for coding mode 1/0: Default: 96000. Minimum: 64000. Maximum: 128000. Valid bitrates for coding mode 1/1: Default: 192000. Minimum: 128000. Maximum: 384000. Valid bitrates for coding mode 2/0: Default: 192000. Minimum: 128000. Maximum: 384000. Valid bitrates for coding mode 3/2 with FLE: Default: 384000. Minimum: 384000. Maximum: 640000."""
    bitstream_mode: NotRequired[
        "capo_mediaconvert.types.ac3_bitstream_mode.Ac3BitstreamMode"
    ]
    """Specify the bitstream mode for the AC-3 stream that the encoder emits. For more information about the AC3 bitstream mode, see ATSC A/52-2012 (Annex E)."""
    coding_mode: NotRequired["capo_mediaconvert.types.ac3_coding_mode.Ac3CodingMode"]
    """Dolby Digital coding mode. Determines number of channels."""
    dialnorm: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max31.__integerMin1Max31"
    ]
    """Sets the dialnorm for the output. If blank and input audio is Dolby Digital, dialnorm will be passed through."""
    dynamic_range_compression_line: NotRequired[
        "capo_mediaconvert.types.ac3_dynamic_range_compression_line.Ac3DynamicRangeCompressionLine"
    ]
    """Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
    dynamic_range_compression_profile: NotRequired[
        "capo_mediaconvert.types.ac3_dynamic_range_compression_profile.Ac3DynamicRangeCompressionProfile"
    ]
    """When you want to add Dolby dynamic range compression (DRC) signaling to your output stream, we recommend that you use the mode-specific settings instead of Dynamic range compression profile. The mode-specific settings are Dynamic range compression profile, line mode and Dynamic range compression profile, RF mode. Note that when you specify values for all three settings, MediaConvert ignores the value of this setting in favor of the mode-specific settings. If you do use this setting instead of the mode-specific settings, choose None to leave out DRC signaling. Keep the default Film standard to set the profile to Dolby's film standard profile for all operating modes."""
    dynamic_range_compression_rf: NotRequired[
        "capo_mediaconvert.types.ac3_dynamic_range_compression_rf.Ac3DynamicRangeCompressionRf"
    ]
    """Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
    lfe_filter: NotRequired["capo_mediaconvert.types.ac3_lfe_filter.Ac3LfeFilter"]
    """Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode."""
    metadata_control: NotRequired[
        "capo_mediaconvert.types.ac3_metadata_control.Ac3MetadataControl"
    ]
    """When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used."""
    sample_rate: NotRequired[
        "capo_mediaconvert.types.__integer_min48000_max48000.__integerMin48000Max48000"
    ]
    """This value is always 48000. It represents the sample rate in Hz."""


# --- restJson1 ser/de ---
def serialize_json(value: Ac3Settings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "bitstream_mode" in value:
        import capo_mediaconvert.types.ac3_bitstream_mode

        out["bitstreamMode"] = (
            capo_mediaconvert.types.ac3_bitstream_mode.serialize_json(
                value["bitstream_mode"]
            )
        )
    if "coding_mode" in value:
        import capo_mediaconvert.types.ac3_coding_mode

        out["codingMode"] = capo_mediaconvert.types.ac3_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "dialnorm" in value:
        out["dialnorm"] = value["dialnorm"]
    if "dynamic_range_compression_line" in value:
        import capo_mediaconvert.types.ac3_dynamic_range_compression_line

        out["dynamicRangeCompressionLine"] = (
            capo_mediaconvert.types.ac3_dynamic_range_compression_line.serialize_json(
                value["dynamic_range_compression_line"]
            )
        )
    if "dynamic_range_compression_profile" in value:
        import capo_mediaconvert.types.ac3_dynamic_range_compression_profile

        out["dynamicRangeCompressionProfile"] = (
            capo_mediaconvert.types.ac3_dynamic_range_compression_profile.serialize_json(
                value["dynamic_range_compression_profile"]
            )
        )
    if "dynamic_range_compression_rf" in value:
        import capo_mediaconvert.types.ac3_dynamic_range_compression_rf

        out["dynamicRangeCompressionRf"] = (
            capo_mediaconvert.types.ac3_dynamic_range_compression_rf.serialize_json(
                value["dynamic_range_compression_rf"]
            )
        )
    if "lfe_filter" in value:
        import capo_mediaconvert.types.ac3_lfe_filter

        out["lfeFilter"] = capo_mediaconvert.types.ac3_lfe_filter.serialize_json(
            value["lfe_filter"]
        )
    if "metadata_control" in value:
        import capo_mediaconvert.types.ac3_metadata_control

        out["metadataControl"] = (
            capo_mediaconvert.types.ac3_metadata_control.serialize_json(
                value["metadata_control"]
            )
        )
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> Ac3Settings:
    out: Ac3Settings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "bitstreamMode" in data:
        import capo_mediaconvert.types.ac3_bitstream_mode

        out["bitstream_mode"] = (
            capo_mediaconvert.types.ac3_bitstream_mode.deserialize_json(
                data["bitstreamMode"]
            )
        )
    if "codingMode" in data:
        import capo_mediaconvert.types.ac3_coding_mode

        out["coding_mode"] = capo_mediaconvert.types.ac3_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if "dialnorm" in data:
        out["dialnorm"] = data["dialnorm"]
    if "dynamicRangeCompressionLine" in data:
        import capo_mediaconvert.types.ac3_dynamic_range_compression_line

        out["dynamic_range_compression_line"] = (
            capo_mediaconvert.types.ac3_dynamic_range_compression_line.deserialize_json(
                data["dynamicRangeCompressionLine"]
            )
        )
    if "dynamicRangeCompressionProfile" in data:
        import capo_mediaconvert.types.ac3_dynamic_range_compression_profile

        out["dynamic_range_compression_profile"] = (
            capo_mediaconvert.types.ac3_dynamic_range_compression_profile.deserialize_json(
                data["dynamicRangeCompressionProfile"]
            )
        )
    if "dynamicRangeCompressionRf" in data:
        import capo_mediaconvert.types.ac3_dynamic_range_compression_rf

        out["dynamic_range_compression_rf"] = (
            capo_mediaconvert.types.ac3_dynamic_range_compression_rf.deserialize_json(
                data["dynamicRangeCompressionRf"]
            )
        )
    if "lfeFilter" in data:
        import capo_mediaconvert.types.ac3_lfe_filter

        out["lfe_filter"] = capo_mediaconvert.types.ac3_lfe_filter.deserialize_json(
            data["lfeFilter"]
        )
    if "metadataControl" in data:
        import capo_mediaconvert.types.ac3_metadata_control

        out["metadata_control"] = (
            capo_mediaconvert.types.ac3_metadata_control.deserialize_json(
                data["metadataControl"]
            )
        )
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
