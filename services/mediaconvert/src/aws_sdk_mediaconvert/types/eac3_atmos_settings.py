"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double_min_negative6_max3
    import aws_sdk_mediaconvert.types.__double_min_negative60_max_negative1
    import aws_sdk_mediaconvert.types.__integer_min0_max100
    import aws_sdk_mediaconvert.types.__integer_min48000_max48000
    import aws_sdk_mediaconvert.types.__integer_min384000_max1024000
    import aws_sdk_mediaconvert.types.eac3_atmos_bitstream_mode
    import aws_sdk_mediaconvert.types.eac3_atmos_coding_mode
    import aws_sdk_mediaconvert.types.eac3_atmos_dialogue_intelligence
    import aws_sdk_mediaconvert.types.eac3_atmos_downmix_control
    import aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_line
    import aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_rf
    import aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_control
    import aws_sdk_mediaconvert.types.eac3_atmos_metering_mode
    import aws_sdk_mediaconvert.types.eac3_atmos_stereo_downmix
    import aws_sdk_mediaconvert.types.eac3_atmos_surround_ex_mode


class Eac3AtmosSettings(TypedDict, closed=True):
    bitrate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min384000_max1024000.__integerMin384000Max1024000"
    ]
    """Specify the average bitrate for this output in bits per second. Valid values: 384k, 448k, 576k, 640k, 768k, 1024k Default value: 448k Note that MediaConvert supports 384k only with channel-based immersive (CBI) 7.1.4 and 5.1.4 inputs. For CBI 9.1.6 and other input types, MediaConvert automatically increases your output bitrate to 448k."""
    bitstream_mode: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_bitstream_mode.Eac3AtmosBitstreamMode"
    ]
    """Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E)."""
    coding_mode: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_coding_mode.Eac3AtmosCodingMode"
    ]
    """The coding mode for Dolby Digital Plus JOC (Atmos)."""
    dialogue_intelligence: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_dialogue_intelligence.Eac3AtmosDialogueIntelligence"
    ]
    """Enable Dolby Dialogue Intelligence to adjust loudness based on dialogue analysis."""
    downmix_control: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_downmix_control.Eac3AtmosDownmixControl"
    ]
    """Specify whether MediaConvert should use any downmix metadata from your input file. Keep the default value, Custom to provide downmix values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your downmix values: Left only/Right only surround, Left total/Right total surround, Left total/Right total center, Left only/Right only center, and Stereo downmix. When you keep Custom for Downmix control and you don't specify values for the related settings, MediaConvert uses default values for those settings."""
    dynamic_range_compression_line: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_line.Eac3AtmosDynamicRangeCompressionLine"
    ]
    """Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the line operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression line. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
    dynamic_range_compression_rf: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_rf.Eac3AtmosDynamicRangeCompressionRf"
    ]
    """Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the RF operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression RF. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf."""
    dynamic_range_control: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_control.Eac3AtmosDynamicRangeControl"
    ]
    """Specify whether MediaConvert should use any dynamic range control metadata from your input file. Keep the default value, Custom, to provide dynamic range control values in your job settings. Choose Follow source to use the metadata from your input. Related settings--Use these settings to specify your dynamic range control values: Dynamic range compression line and Dynamic range compression RF. When you keep the value Custom for Dynamic range control and you don't specify values for the related settings, MediaConvert uses default values for those settings."""
    lo_ro_center_mix_level: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min_negative6_max3.__doubleMinNegative6Max3"
    ]
    """Specify a value for the following Dolby Atmos setting: Left only/Right only center mix (Lo/Ro center). MediaConvert uses this value for downmixing. Default value: -3 dB. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, and -6.0. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left only/Right only center."""
    lo_ro_surround_mix_level: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min_negative60_max_negative1.__doubleMinNegative60MaxNegative1"
    ]
    """Specify a value for the following Dolby Atmos setting: Left only/Right only. MediaConvert uses this value for downmixing. Default value: -3 dB. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left only/Right only surround."""
    lt_rt_center_mix_level: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min_negative6_max3.__doubleMinNegative6Max3"
    ]
    """Specify a value for the following Dolby Atmos setting: Left total/Right total center mix (Lt/Rt center). MediaConvert uses this value for downmixing. Default value: -3 dB Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, and -6.0. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left total/Right total center."""
    lt_rt_surround_mix_level: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min_negative60_max_negative1.__doubleMinNegative60MaxNegative1"
    ]
    """Specify a value for the following Dolby Atmos setting: Left total/Right total surround mix (Lt/Rt surround). MediaConvert uses this value for downmixing. Default value: -3 dB Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, the service ignores Left total/Right total surround."""
    metering_mode: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_metering_mode.Eac3AtmosMeteringMode"
    ]
    """Choose how the service meters the loudness of your audio."""
    sample_rate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min48000_max48000.__integerMin48000Max48000"
    ]
    """This value is always 48000. It represents the sample rate in Hz."""
    speech_threshold: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Specify the percentage of audio content, from 0% to 100%, that must be speech in order for the encoder to use the measured speech loudness as the overall program loudness. Default value: 15%"""
    stereo_downmix: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_stereo_downmix.Eac3AtmosStereoDownmix"
    ]
    """Choose how the service does stereo downmixing. Default value: Not indicated Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Stereo downmix."""
    surround_ex_mode: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_surround_ex_mode.Eac3AtmosSurroundExMode"
    ]
    """Specify whether your input audio has an additional center rear surround channel matrix encoded into your left and right surround channels."""


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosSettings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "bitstream_mode" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_bitstream_mode

        out["bitstreamMode"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_bitstream_mode.serialize_json(
                value["bitstream_mode"]
            )
        )
    if "coding_mode" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_coding_mode

        out["codingMode"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_coding_mode.serialize_json(
                value["coding_mode"]
            )
        )
    if "dialogue_intelligence" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_dialogue_intelligence

        out["dialogueIntelligence"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_dialogue_intelligence.serialize_json(
                value["dialogue_intelligence"]
            )
        )
    if "downmix_control" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_downmix_control

        out["downmixControl"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_downmix_control.serialize_json(
                value["downmix_control"]
            )
        )
    if "dynamic_range_compression_line" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_line

        out["dynamicRangeCompressionLine"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_line.serialize_json(
                value["dynamic_range_compression_line"]
            )
        )
    if "dynamic_range_compression_rf" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_rf

        out["dynamicRangeCompressionRf"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_rf.serialize_json(
                value["dynamic_range_compression_rf"]
            )
        )
    if "dynamic_range_control" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_control

        out["dynamicRangeControl"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_control.serialize_json(
                value["dynamic_range_control"]
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
    if "metering_mode" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_metering_mode

        out["meteringMode"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_metering_mode.serialize_json(
                value["metering_mode"]
            )
        )
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "speech_threshold" in value:
        out["speechThreshold"] = value["speech_threshold"]
    if "stereo_downmix" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_stereo_downmix

        out["stereoDownmix"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_stereo_downmix.serialize_json(
                value["stereo_downmix"]
            )
        )
    if "surround_ex_mode" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_surround_ex_mode

        out["surroundExMode"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_surround_ex_mode.serialize_json(
                value["surround_ex_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> Eac3AtmosSettings:
    out: Eac3AtmosSettings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "bitstreamMode" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_bitstream_mode

        out["bitstream_mode"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_bitstream_mode.deserialize_json(
                data["bitstreamMode"]
            )
        )
    if "codingMode" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_coding_mode

        out["coding_mode"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_coding_mode.deserialize_json(
                data["codingMode"]
            )
        )
    if "dialogueIntelligence" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_dialogue_intelligence

        out["dialogue_intelligence"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_dialogue_intelligence.deserialize_json(
                data["dialogueIntelligence"]
            )
        )
    if "downmixControl" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_downmix_control

        out["downmix_control"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_downmix_control.deserialize_json(
                data["downmixControl"]
            )
        )
    if "dynamicRangeCompressionLine" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_line

        out["dynamic_range_compression_line"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_line.deserialize_json(
                data["dynamicRangeCompressionLine"]
            )
        )
    if "dynamicRangeCompressionRf" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_rf

        out["dynamic_range_compression_rf"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_compression_rf.deserialize_json(
                data["dynamicRangeCompressionRf"]
            )
        )
    if "dynamicRangeControl" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_control

        out["dynamic_range_control"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_dynamic_range_control.deserialize_json(
                data["dynamicRangeControl"]
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
    if "meteringMode" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_metering_mode

        out["metering_mode"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_metering_mode.deserialize_json(
                data["meteringMode"]
            )
        )
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    if "speechThreshold" in data:
        out["speech_threshold"] = data["speechThreshold"]
    if "stereoDownmix" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_stereo_downmix

        out["stereo_downmix"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_stereo_downmix.deserialize_json(
                data["stereoDownmix"]
            )
        )
    if "surroundExMode" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_surround_ex_mode

        out["surround_ex_mode"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_surround_ex_mode.deserialize_json(
                data["surroundExMode"]
            )
        )
    return out
