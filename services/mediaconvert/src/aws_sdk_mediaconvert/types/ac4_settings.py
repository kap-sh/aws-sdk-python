"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac4Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double_min_negative1000_max3
    import aws_sdk_mediaconvert.types.__double_min_negative1000_max_negative1
    import aws_sdk_mediaconvert.types.__integer_min48000_max48000
    import aws_sdk_mediaconvert.types.__integer_min48000_max768000
    import aws_sdk_mediaconvert.types.ac4_bitstream_mode
    import aws_sdk_mediaconvert.types.ac4_coding_mode
    import aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile
    import aws_sdk_mediaconvert.types.ac4_stereo_downmix


class Ac4Settings(TypedDict, closed=True):
    bitrate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min48000_max768000.__integerMin48000Max768000"
    ]
    """Specify the average bitrate in bits per second. Leave blank to use the default bitrate for the coding mode you select according to ETSI TS 103 190. Valid bitrates for coding mode 2.0 (stereo): 48000, 64000, 96000, 128000, 144000, 192000, 256000, 288000, 320000, 384000, 448000, 512000, or 768000. Valid bitrates for coding mode 5.1 (3/2 with LFE): 96000, 128000, 144000, 192000, 256000, 288000, 320000, 384000, 448000, 512000, or 768000. Valid bitrates for coding mode 5.1.4 (immersive): 192000, 256000, 288000, 320000, 384000, 448000, 512000, or 768000."""
    bitstream_mode: NotRequired[
        "aws_sdk_mediaconvert.types.ac4_bitstream_mode.Ac4BitstreamMode"
    ]
    """Specify the bitstream mode for the AC-4 stream that the encoder emits. For more information about the AC-4 bitstream mode, see ETSI TS 103 190. Maps to dlb_paec_ac4_bed_classifier in the encoder implementation. - COMPLETE_MAIN: Complete Main (standard mix) - EMERGENCY: Stereo Emergency content"""
    coding_mode: NotRequired["aws_sdk_mediaconvert.types.ac4_coding_mode.Ac4CodingMode"]
    """Dolby AC-4 coding mode. Determines number of channels. Maps to dlb_paec_ac4_bed_channel_config in the encoder implementation. - CODING_MODE_2_0: 2.0 (stereo) - maps to DLB_PAEC_AC4_BED_CHANNEL_CONFIG_20 - CODING_MODE_3_2_LFE: 5.1 surround - maps to DLB_PAEC_AC4_BED_CHANNEL_CONFIG_51 - CODING_MODE_5_1_4: 5.1.4 immersive - maps to DLB_PAEC_AC4_BED_CHANNEL_CONFIG_514"""
    dynamic_range_compression_flat_panel_tv: NotRequired[
        "aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.Ac4DynamicRangeCompressionDrcProfile"
    ]
    """Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification."""
    dynamic_range_compression_home_theater: NotRequired[
        "aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.Ac4DynamicRangeCompressionDrcProfile"
    ]
    """Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification."""
    dynamic_range_compression_portable_headphones: NotRequired[
        "aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.Ac4DynamicRangeCompressionDrcProfile"
    ]
    """Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification."""
    dynamic_range_compression_portable_speakers: NotRequired[
        "aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.Ac4DynamicRangeCompressionDrcProfile"
    ]
    """Choose the Dolby AC-4 dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby AC-4 stream for the specified decoder mode. For information about the Dolby AC-4 DRC profiles, see the Dolby AC-4 specification."""
    lo_ro_center_mix_level: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min_negative1000_max3.__doubleMinNegative1000Max3"
    ]
    """Specify a value for the following Dolby AC-4 setting: Left only/Right only center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only center."""
    lo_ro_surround_mix_level: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min_negative1000_max_negative1.__doubleMinNegative1000MaxNegative1"
    ]
    """Specify a value for the following Dolby AC-4 setting: Left only/Right only surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only surround."""
    lt_rt_center_mix_level: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min_negative1000_max3.__doubleMinNegative1000Max3"
    ]
    """Specify a value for the following Dolby AC-4 setting: Left total/Right total center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total center."""
    lt_rt_surround_mix_level: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min_negative1000_max_negative1.__doubleMinNegative1000MaxNegative1"
    ]
    """Specify a value for the following Dolby AC-4 setting: Left total/Right total surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -infinity. The value -infinity mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total surround."""
    sample_rate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min48000_max48000.__integerMin48000Max48000"
    ]
    """This value is always 48000. It represents the sample rate in Hz."""
    stereo_downmix: NotRequired[
        "aws_sdk_mediaconvert.types.ac4_stereo_downmix.Ac4StereoDownmix"
    ]
    """Choose the preferred stereo downmix method. This setting tells the decoder how to downmix multi-channel audio to stereo during playback."""


# --- restJson1 ser/de ---
def serialize_json(value: Ac4Settings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "bitstream_mode" in value:
        import aws_sdk_mediaconvert.types.ac4_bitstream_mode

        out["bitstreamMode"] = (
            aws_sdk_mediaconvert.types.ac4_bitstream_mode.serialize_json(
                value["bitstream_mode"]
            )
        )
    if "coding_mode" in value:
        import aws_sdk_mediaconvert.types.ac4_coding_mode

        out["codingMode"] = aws_sdk_mediaconvert.types.ac4_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "dynamic_range_compression_flat_panel_tv" in value:
        import aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile

        out["dynamicRangeCompressionFlatPanelTv"] = (
            aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.serialize_json(
                value["dynamic_range_compression_flat_panel_tv"]
            )
        )
    if "dynamic_range_compression_home_theater" in value:
        import aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile

        out["dynamicRangeCompressionHomeTheater"] = (
            aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.serialize_json(
                value["dynamic_range_compression_home_theater"]
            )
        )
    if "dynamic_range_compression_portable_headphones" in value:
        import aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile

        out["dynamicRangeCompressionPortableHeadphones"] = (
            aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.serialize_json(
                value["dynamic_range_compression_portable_headphones"]
            )
        )
    if "dynamic_range_compression_portable_speakers" in value:
        import aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile

        out["dynamicRangeCompressionPortableSpeakers"] = (
            aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.serialize_json(
                value["dynamic_range_compression_portable_speakers"]
            )
        )
    if "lo_ro_center_mix_level" in value:
        out["loRoCenterMixLevel"] = value["lo_ro_center_mix_level"]
    if "lo_ro_surround_mix_level" in value:
        out["loRoSurroundMixLevel"] = value["lo_ro_surround_mix_level"]
    if "lt_rt_center_mix_level" in value:
        out["ltRtCenterMixLevel"] = value["lt_rt_center_mix_level"]
    if "lt_rt_surround_mix_level" in value:
        out["ltRtSurroundMixLevel"] = value["lt_rt_surround_mix_level"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "stereo_downmix" in value:
        import aws_sdk_mediaconvert.types.ac4_stereo_downmix

        out["stereoDownmix"] = (
            aws_sdk_mediaconvert.types.ac4_stereo_downmix.serialize_json(
                value["stereo_downmix"]
            )
        )
    return out


def deserialize_json(data: dict) -> Ac4Settings:
    out: Ac4Settings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "bitstreamMode" in data:
        import aws_sdk_mediaconvert.types.ac4_bitstream_mode

        out["bitstream_mode"] = (
            aws_sdk_mediaconvert.types.ac4_bitstream_mode.deserialize_json(
                data["bitstreamMode"]
            )
        )
    if "codingMode" in data:
        import aws_sdk_mediaconvert.types.ac4_coding_mode

        out["coding_mode"] = (
            aws_sdk_mediaconvert.types.ac4_coding_mode.deserialize_json(
                data["codingMode"]
            )
        )
    if "dynamicRangeCompressionFlatPanelTv" in data:
        import aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile

        out["dynamic_range_compression_flat_panel_tv"] = (
            aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.deserialize_json(
                data["dynamicRangeCompressionFlatPanelTv"]
            )
        )
    if "dynamicRangeCompressionHomeTheater" in data:
        import aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile

        out["dynamic_range_compression_home_theater"] = (
            aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.deserialize_json(
                data["dynamicRangeCompressionHomeTheater"]
            )
        )
    if "dynamicRangeCompressionPortableHeadphones" in data:
        import aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile

        out["dynamic_range_compression_portable_headphones"] = (
            aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.deserialize_json(
                data["dynamicRangeCompressionPortableHeadphones"]
            )
        )
    if "dynamicRangeCompressionPortableSpeakers" in data:
        import aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile

        out["dynamic_range_compression_portable_speakers"] = (
            aws_sdk_mediaconvert.types.ac4_dynamic_range_compression_drc_profile.deserialize_json(
                data["dynamicRangeCompressionPortableSpeakers"]
            )
        )
    if "loRoCenterMixLevel" in data:
        out["lo_ro_center_mix_level"] = data["loRoCenterMixLevel"]
    if "loRoSurroundMixLevel" in data:
        out["lo_ro_surround_mix_level"] = data["loRoSurroundMixLevel"]
    if "ltRtCenterMixLevel" in data:
        out["lt_rt_center_mix_level"] = data["ltRtCenterMixLevel"]
    if "ltRtSurroundMixLevel" in data:
        out["lt_rt_surround_mix_level"] = data["ltRtSurroundMixLevel"]
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    if "stereoDownmix" in data:
        import aws_sdk_mediaconvert.types.ac4_stereo_downmix

        out["stereo_downmix"] = (
            aws_sdk_mediaconvert.types.ac4_stereo_downmix.deserialize_json(
                data["stereoDownmix"]
            )
        )
    return out
