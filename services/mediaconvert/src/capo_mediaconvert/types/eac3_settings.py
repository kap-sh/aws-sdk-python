"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double_min_negative60_max3
    import capo_mediaconvert.types.__double_min_negative60_max_negative1
    import capo_mediaconvert.types.__integer_min1_max31
    import capo_mediaconvert.types.__integer_min32000_max3024000
    import capo_mediaconvert.types.__integer_min48000_max48000
    import capo_mediaconvert.types.eac3_attenuation_control
    import capo_mediaconvert.types.eac3_bitstream_mode
    import capo_mediaconvert.types.eac3_coding_mode
    import capo_mediaconvert.types.eac3_dc_filter
    import capo_mediaconvert.types.eac3_dynamic_range_compression_line
    import capo_mediaconvert.types.eac3_dynamic_range_compression_rf
    import capo_mediaconvert.types.eac3_lfe_control
    import capo_mediaconvert.types.eac3_lfe_filter
    import capo_mediaconvert.types.eac3_metadata_control
    import capo_mediaconvert.types.eac3_passthrough_control
    import capo_mediaconvert.types.eac3_phase_control
    import capo_mediaconvert.types.eac3_stereo_downmix
    import capo_mediaconvert.types.eac3_surround_ex_mode
    import capo_mediaconvert.types.eac3_surround_mode


class Eac3Settings(TypedDict, closed=True):
    attenuation_control: NotRequired[
        "capo_mediaconvert.types.eac3_attenuation_control.Eac3AttenuationControl"
    ]
    """If set to ATTENUATE_3_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode."""
    bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min32000_max3024000.__integerMin32000Max3024000"
    ]
    """Specify the average bitrate in bits per second. The bitrate that you specify must be a multiple of 8000 within the allowed minimum and maximum values. Leave blank to use the default bitrate for the coding mode you select according ETSI TS 102 366. Valid bitrates for coding mode 1/0: Default: 96000. Minimum: 32000. Maximum: 3024000. Valid bitrates for coding mode 2/0: Default: 192000. Minimum: 96000. Maximum: 3024000. Valid bitrates for coding mode 3/2: Default: 384000. Minimum: 192000. Maximum: 3024000."""
    bitstream_mode: NotRequired[
        "capo_mediaconvert.types.eac3_bitstream_mode.Eac3BitstreamMode"
    ]
    """Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E)."""
    coding_mode: NotRequired["capo_mediaconvert.types.eac3_coding_mode.Eac3CodingMode"]
    """Dolby Digital Plus coding mode. Determines number of channels."""
    dc_filter: NotRequired["capo_mediaconvert.types.eac3_dc_filter.Eac3DcFilter"]
    """Activates a DC highpass filter for all input channels."""
    dialnorm: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max31.__integerMin1Max31"
    ]
    """Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through."""
    dynamic_range_compression_line: NotRequired[
        "capo_mediaconvert.types.eac3_dynamic_range_compression_line.Eac3DynamicRangeCompressionLine"
    ]
    """Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
    dynamic_range_compression_rf: NotRequired[
        "capo_mediaconvert.types.eac3_dynamic_range_compression_rf.Eac3DynamicRangeCompressionRf"
    ]
    """Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
    lfe_control: NotRequired["capo_mediaconvert.types.eac3_lfe_control.Eac3LfeControl"]
    """When encoding 3/2 audio, controls whether the LFE channel is enabled"""
    lfe_filter: NotRequired["capo_mediaconvert.types.eac3_lfe_filter.Eac3LfeFilter"]
    """Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode."""
    lo_ro_center_mix_level: NotRequired[
        "capo_mediaconvert.types.__double_min_negative60_max3.__doubleMinNegative60Max3"
    ]
    """Specify a value for the following Dolby Digital Plus setting: Left only/Right only center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only center."""
    lo_ro_surround_mix_level: NotRequired[
        "capo_mediaconvert.types.__double_min_negative60_max_negative1.__doubleMinNegative60MaxNegative1"
    ]
    """Specify a value for the following Dolby Digital Plus setting: Left only/Right only. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only surround."""
    lt_rt_center_mix_level: NotRequired[
        "capo_mediaconvert.types.__double_min_negative60_max3.__doubleMinNegative60Max3"
    ]
    """Specify a value for the following Dolby Digital Plus setting: Left total/Right total center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total center."""
    lt_rt_surround_mix_level: NotRequired[
        "capo_mediaconvert.types.__double_min_negative60_max_negative1.__doubleMinNegative60MaxNegative1"
    ]
    """Specify a value for the following Dolby Digital Plus setting: Left total/Right total surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total surround."""
    metadata_control: NotRequired[
        "capo_mediaconvert.types.eac3_metadata_control.Eac3MetadataControl"
    ]
    """When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used."""
    passthrough_control: NotRequired[
        "capo_mediaconvert.types.eac3_passthrough_control.Eac3PassthroughControl"
    ]
    """When set to WHEN_POSSIBLE, input DD+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding."""
    phase_control: NotRequired[
        "capo_mediaconvert.types.eac3_phase_control.Eac3PhaseControl"
    ]
    """Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode."""
    sample_rate: NotRequired[
        "capo_mediaconvert.types.__integer_min48000_max48000.__integerMin48000Max48000"
    ]
    """This value is always 48000. It represents the sample rate in Hz."""
    stereo_downmix: NotRequired[
        "capo_mediaconvert.types.eac3_stereo_downmix.Eac3StereoDownmix"
    ]
    """Choose how the service does stereo downmixing. This setting only applies if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Stereo downmix."""
    surround_ex_mode: NotRequired[
        "capo_mediaconvert.types.eac3_surround_ex_mode.Eac3SurroundExMode"
    ]
    """When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels."""
    surround_mode: NotRequired[
        "capo_mediaconvert.types.eac3_surround_mode.Eac3SurroundMode"
    ]
    """When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels."""


# --- restJson1 ser/de ---
def serialize_json(value: Eac3Settings) -> dict:
    out: dict = {}
    if "attenuation_control" in value:
        import capo_mediaconvert.types.eac3_attenuation_control

        out["attenuationControl"] = (
            capo_mediaconvert.types.eac3_attenuation_control.serialize_json(
                value["attenuation_control"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "bitstream_mode" in value:
        import capo_mediaconvert.types.eac3_bitstream_mode

        out["bitstreamMode"] = (
            capo_mediaconvert.types.eac3_bitstream_mode.serialize_json(
                value["bitstream_mode"]
            )
        )
    if "coding_mode" in value:
        import capo_mediaconvert.types.eac3_coding_mode

        out["codingMode"] = capo_mediaconvert.types.eac3_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "dc_filter" in value:
        import capo_mediaconvert.types.eac3_dc_filter

        out["dcFilter"] = capo_mediaconvert.types.eac3_dc_filter.serialize_json(
            value["dc_filter"]
        )
    if "dialnorm" in value:
        out["dialnorm"] = value["dialnorm"]
    if "dynamic_range_compression_line" in value:
        import capo_mediaconvert.types.eac3_dynamic_range_compression_line

        out["dynamicRangeCompressionLine"] = (
            capo_mediaconvert.types.eac3_dynamic_range_compression_line.serialize_json(
                value["dynamic_range_compression_line"]
            )
        )
    if "dynamic_range_compression_rf" in value:
        import capo_mediaconvert.types.eac3_dynamic_range_compression_rf

        out["dynamicRangeCompressionRf"] = (
            capo_mediaconvert.types.eac3_dynamic_range_compression_rf.serialize_json(
                value["dynamic_range_compression_rf"]
            )
        )
    if "lfe_control" in value:
        import capo_mediaconvert.types.eac3_lfe_control

        out["lfeControl"] = capo_mediaconvert.types.eac3_lfe_control.serialize_json(
            value["lfe_control"]
        )
    if "lfe_filter" in value:
        import capo_mediaconvert.types.eac3_lfe_filter

        out["lfeFilter"] = capo_mediaconvert.types.eac3_lfe_filter.serialize_json(
            value["lfe_filter"]
        )
    if "lo_ro_center_mix_level" in value:
        out["loRoCenterMixLevel"] = value["lo_ro_center_mix_level"]
    if "lo_ro_surround_mix_level" in value:
        out["loRoSurroundMixLevel"] = value["lo_ro_surround_mix_level"]
    if "lt_rt_center_mix_level" in value:
        out["ltRtCenterMixLevel"] = value["lt_rt_center_mix_level"]
    if "lt_rt_surround_mix_level" in value:
        out["ltRtSurroundMixLevel"] = value["lt_rt_surround_mix_level"]
    if "metadata_control" in value:
        import capo_mediaconvert.types.eac3_metadata_control

        out["metadataControl"] = (
            capo_mediaconvert.types.eac3_metadata_control.serialize_json(
                value["metadata_control"]
            )
        )
    if "passthrough_control" in value:
        import capo_mediaconvert.types.eac3_passthrough_control

        out["passthroughControl"] = (
            capo_mediaconvert.types.eac3_passthrough_control.serialize_json(
                value["passthrough_control"]
            )
        )
    if "phase_control" in value:
        import capo_mediaconvert.types.eac3_phase_control

        out["phaseControl"] = capo_mediaconvert.types.eac3_phase_control.serialize_json(
            value["phase_control"]
        )
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "stereo_downmix" in value:
        import capo_mediaconvert.types.eac3_stereo_downmix

        out["stereoDownmix"] = (
            capo_mediaconvert.types.eac3_stereo_downmix.serialize_json(
                value["stereo_downmix"]
            )
        )
    if "surround_ex_mode" in value:
        import capo_mediaconvert.types.eac3_surround_ex_mode

        out["surroundExMode"] = (
            capo_mediaconvert.types.eac3_surround_ex_mode.serialize_json(
                value["surround_ex_mode"]
            )
        )
    if "surround_mode" in value:
        import capo_mediaconvert.types.eac3_surround_mode

        out["surroundMode"] = capo_mediaconvert.types.eac3_surround_mode.serialize_json(
            value["surround_mode"]
        )
    return out


def deserialize_json(data: dict) -> Eac3Settings:
    out: Eac3Settings = {}  # type: ignore[typeddict-item]
    if "attenuationControl" in data:
        import capo_mediaconvert.types.eac3_attenuation_control

        out["attenuation_control"] = (
            capo_mediaconvert.types.eac3_attenuation_control.deserialize_json(
                data["attenuationControl"]
            )
        )
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "bitstreamMode" in data:
        import capo_mediaconvert.types.eac3_bitstream_mode

        out["bitstream_mode"] = (
            capo_mediaconvert.types.eac3_bitstream_mode.deserialize_json(
                data["bitstreamMode"]
            )
        )
    if "codingMode" in data:
        import capo_mediaconvert.types.eac3_coding_mode

        out["coding_mode"] = capo_mediaconvert.types.eac3_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if "dcFilter" in data:
        import capo_mediaconvert.types.eac3_dc_filter

        out["dc_filter"] = capo_mediaconvert.types.eac3_dc_filter.deserialize_json(
            data["dcFilter"]
        )
    if "dialnorm" in data:
        out["dialnorm"] = data["dialnorm"]
    if "dynamicRangeCompressionLine" in data:
        import capo_mediaconvert.types.eac3_dynamic_range_compression_line

        out["dynamic_range_compression_line"] = (
            capo_mediaconvert.types.eac3_dynamic_range_compression_line.deserialize_json(
                data["dynamicRangeCompressionLine"]
            )
        )
    if "dynamicRangeCompressionRf" in data:
        import capo_mediaconvert.types.eac3_dynamic_range_compression_rf

        out["dynamic_range_compression_rf"] = (
            capo_mediaconvert.types.eac3_dynamic_range_compression_rf.deserialize_json(
                data["dynamicRangeCompressionRf"]
            )
        )
    if "lfeControl" in data:
        import capo_mediaconvert.types.eac3_lfe_control

        out["lfe_control"] = capo_mediaconvert.types.eac3_lfe_control.deserialize_json(
            data["lfeControl"]
        )
    if "lfeFilter" in data:
        import capo_mediaconvert.types.eac3_lfe_filter

        out["lfe_filter"] = capo_mediaconvert.types.eac3_lfe_filter.deserialize_json(
            data["lfeFilter"]
        )
    if "loRoCenterMixLevel" in data:
        out["lo_ro_center_mix_level"] = data["loRoCenterMixLevel"]
    if "loRoSurroundMixLevel" in data:
        out["lo_ro_surround_mix_level"] = data["loRoSurroundMixLevel"]
    if "ltRtCenterMixLevel" in data:
        out["lt_rt_center_mix_level"] = data["ltRtCenterMixLevel"]
    if "ltRtSurroundMixLevel" in data:
        out["lt_rt_surround_mix_level"] = data["ltRtSurroundMixLevel"]
    if "metadataControl" in data:
        import capo_mediaconvert.types.eac3_metadata_control

        out["metadata_control"] = (
            capo_mediaconvert.types.eac3_metadata_control.deserialize_json(
                data["metadataControl"]
            )
        )
    if "passthroughControl" in data:
        import capo_mediaconvert.types.eac3_passthrough_control

        out["passthrough_control"] = (
            capo_mediaconvert.types.eac3_passthrough_control.deserialize_json(
                data["passthroughControl"]
            )
        )
    if "phaseControl" in data:
        import capo_mediaconvert.types.eac3_phase_control

        out["phase_control"] = (
            capo_mediaconvert.types.eac3_phase_control.deserialize_json(
                data["phaseControl"]
            )
        )
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    if "stereoDownmix" in data:
        import capo_mediaconvert.types.eac3_stereo_downmix

        out["stereo_downmix"] = (
            capo_mediaconvert.types.eac3_stereo_downmix.deserialize_json(
                data["stereoDownmix"]
            )
        )
    if "surroundExMode" in data:
        import capo_mediaconvert.types.eac3_surround_ex_mode

        out["surround_ex_mode"] = (
            capo_mediaconvert.types.eac3_surround_ex_mode.deserialize_json(
                data["surroundExMode"]
            )
        )
    if "surroundMode" in data:
        import capo_mediaconvert.types.eac3_surround_mode

        out["surround_mode"] = (
            capo_mediaconvert.types.eac3_surround_mode.deserialize_json(
                data["surroundMode"]
            )
        )
    return out
