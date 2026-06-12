"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3Settings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.__integer_min1_max31
    import aws_sdk_medialive.types.eac3_attenuation_control
    import aws_sdk_medialive.types.eac3_bitstream_mode
    import aws_sdk_medialive.types.eac3_coding_mode
    import aws_sdk_medialive.types.eac3_dc_filter
    import aws_sdk_medialive.types.eac3_drc_line
    import aws_sdk_medialive.types.eac3_drc_rf
    import aws_sdk_medialive.types.eac3_lfe_control
    import aws_sdk_medialive.types.eac3_lfe_filter
    import aws_sdk_medialive.types.eac3_metadata_control
    import aws_sdk_medialive.types.eac3_passthrough_control
    import aws_sdk_medialive.types.eac3_phase_control
    import aws_sdk_medialive.types.eac3_stereo_downmix
    import aws_sdk_medialive.types.eac3_surround_ex_mode
    import aws_sdk_medialive.types.eac3_surround_mode


class Eac3Settings(TypedDict):
    attenuation_control: NotRequired[
        "aws_sdk_medialive.types.eac3_attenuation_control.Eac3AttenuationControl"
    ]
    """When set to attenuate3Db, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode."""
    bitrate: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Average bitrate in bits/second. Valid bitrates depend on the coding mode."""
    bitstream_mode: NotRequired[
        "aws_sdk_medialive.types.eac3_bitstream_mode.Eac3BitstreamMode"
    ]
    """Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values."""
    coding_mode: NotRequired["aws_sdk_medialive.types.eac3_coding_mode.Eac3CodingMode"]
    """Dolby Digital Plus coding mode. Determines number of channels."""
    dc_filter: NotRequired["aws_sdk_medialive.types.eac3_dc_filter.Eac3DcFilter"]
    """When set to enabled, activates a DC highpass filter for all input channels."""
    dialnorm: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max31.__integerMin1Max31"
    ]
    """Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through."""
    drc_line: NotRequired["aws_sdk_medialive.types.eac3_drc_line.Eac3DrcLine"]
    """Sets the Dolby dynamic range compression profile."""
    drc_rf: NotRequired["aws_sdk_medialive.types.eac3_drc_rf.Eac3DrcRf"]
    """Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels."""
    lfe_control: NotRequired["aws_sdk_medialive.types.eac3_lfe_control.Eac3LfeControl"]
    """When encoding 3/2 audio, setting to lfe enables the LFE channel"""
    lfe_filter: NotRequired["aws_sdk_medialive.types.eac3_lfe_filter.Eac3LfeFilter"]
    """When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with codingMode32 coding mode."""
    lo_ro_center_mix_level: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Left only/Right only center mix level. Only used for 3/2 coding mode."""
    lo_ro_surround_mix_level: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Left only/Right only surround mix level. Only used for 3/2 coding mode."""
    lt_rt_center_mix_level: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Left total/Right total center mix level. Only used for 3/2 coding mode."""
    lt_rt_surround_mix_level: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Left total/Right total surround mix level. Only used for 3/2 coding mode."""
    metadata_control: NotRequired[
        "aws_sdk_medialive.types.eac3_metadata_control.Eac3MetadataControl"
    ]
    """When set to followInput, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used."""
    passthrough_control: NotRequired[
        "aws_sdk_medialive.types.eac3_passthrough_control.Eac3PassthroughControl"
    ]
    """When set to whenPossible, input DD+ audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding."""
    phase_control: NotRequired[
        "aws_sdk_medialive.types.eac3_phase_control.Eac3PhaseControl"
    ]
    """When set to shift90Degrees, applies a 90-degree phase shift to the surround channels. Only used for 3/2 coding mode."""
    stereo_downmix: NotRequired[
        "aws_sdk_medialive.types.eac3_stereo_downmix.Eac3StereoDownmix"
    ]
    """Stereo downmix preference. Only used for 3/2 coding mode."""
    surround_ex_mode: NotRequired[
        "aws_sdk_medialive.types.eac3_surround_ex_mode.Eac3SurroundExMode"
    ]
    """When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels."""
    surround_mode: NotRequired[
        "aws_sdk_medialive.types.eac3_surround_mode.Eac3SurroundMode"
    ]
    """When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels."""


# --- restJson1 ser/de ---
def serialize_json(value: Eac3Settings) -> dict:
    out: dict = {}
    if "attenuation_control" in value:
        import aws_sdk_medialive.types.eac3_attenuation_control

        out["attenuationControl"] = (
            aws_sdk_medialive.types.eac3_attenuation_control.serialize_json(
                value["attenuation_control"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "bitstream_mode" in value:
        import aws_sdk_medialive.types.eac3_bitstream_mode

        out["bitstreamMode"] = (
            aws_sdk_medialive.types.eac3_bitstream_mode.serialize_json(
                value["bitstream_mode"]
            )
        )
    if "coding_mode" in value:
        import aws_sdk_medialive.types.eac3_coding_mode

        out["codingMode"] = aws_sdk_medialive.types.eac3_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "dc_filter" in value:
        import aws_sdk_medialive.types.eac3_dc_filter

        out["dcFilter"] = aws_sdk_medialive.types.eac3_dc_filter.serialize_json(
            value["dc_filter"]
        )
    if "dialnorm" in value:
        out["dialnorm"] = value["dialnorm"]
    if "drc_line" in value:
        import aws_sdk_medialive.types.eac3_drc_line

        out["drcLine"] = aws_sdk_medialive.types.eac3_drc_line.serialize_json(
            value["drc_line"]
        )
    if "drc_rf" in value:
        import aws_sdk_medialive.types.eac3_drc_rf

        out["drcRf"] = aws_sdk_medialive.types.eac3_drc_rf.serialize_json(
            value["drc_rf"]
        )
    if "lfe_control" in value:
        import aws_sdk_medialive.types.eac3_lfe_control

        out["lfeControl"] = aws_sdk_medialive.types.eac3_lfe_control.serialize_json(
            value["lfe_control"]
        )
    if "lfe_filter" in value:
        import aws_sdk_medialive.types.eac3_lfe_filter

        out["lfeFilter"] = aws_sdk_medialive.types.eac3_lfe_filter.serialize_json(
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
        import aws_sdk_medialive.types.eac3_metadata_control

        out["metadataControl"] = (
            aws_sdk_medialive.types.eac3_metadata_control.serialize_json(
                value["metadata_control"]
            )
        )
    if "passthrough_control" in value:
        import aws_sdk_medialive.types.eac3_passthrough_control

        out["passthroughControl"] = (
            aws_sdk_medialive.types.eac3_passthrough_control.serialize_json(
                value["passthrough_control"]
            )
        )
    if "phase_control" in value:
        import aws_sdk_medialive.types.eac3_phase_control

        out["phaseControl"] = aws_sdk_medialive.types.eac3_phase_control.serialize_json(
            value["phase_control"]
        )
    if "stereo_downmix" in value:
        import aws_sdk_medialive.types.eac3_stereo_downmix

        out["stereoDownmix"] = (
            aws_sdk_medialive.types.eac3_stereo_downmix.serialize_json(
                value["stereo_downmix"]
            )
        )
    if "surround_ex_mode" in value:
        import aws_sdk_medialive.types.eac3_surround_ex_mode

        out["surroundExMode"] = (
            aws_sdk_medialive.types.eac3_surround_ex_mode.serialize_json(
                value["surround_ex_mode"]
            )
        )
    if "surround_mode" in value:
        import aws_sdk_medialive.types.eac3_surround_mode

        out["surroundMode"] = aws_sdk_medialive.types.eac3_surround_mode.serialize_json(
            value["surround_mode"]
        )
    return out


def deserialize_json(data: dict) -> Eac3Settings:
    out: Eac3Settings = {}  # type: ignore[typeddict-item]
    if "attenuationControl" in data:
        import aws_sdk_medialive.types.eac3_attenuation_control

        out["attenuation_control"] = (
            aws_sdk_medialive.types.eac3_attenuation_control.deserialize_json(
                data["attenuationControl"]
            )
        )
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "bitstreamMode" in data:
        import aws_sdk_medialive.types.eac3_bitstream_mode

        out["bitstream_mode"] = (
            aws_sdk_medialive.types.eac3_bitstream_mode.deserialize_json(
                data["bitstreamMode"]
            )
        )
    if "codingMode" in data:
        import aws_sdk_medialive.types.eac3_coding_mode

        out["coding_mode"] = aws_sdk_medialive.types.eac3_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if "dcFilter" in data:
        import aws_sdk_medialive.types.eac3_dc_filter

        out["dc_filter"] = aws_sdk_medialive.types.eac3_dc_filter.deserialize_json(
            data["dcFilter"]
        )
    if "dialnorm" in data:
        out["dialnorm"] = data["dialnorm"]
    if "drcLine" in data:
        import aws_sdk_medialive.types.eac3_drc_line

        out["drc_line"] = aws_sdk_medialive.types.eac3_drc_line.deserialize_json(
            data["drcLine"]
        )
    if "drcRf" in data:
        import aws_sdk_medialive.types.eac3_drc_rf

        out["drc_rf"] = aws_sdk_medialive.types.eac3_drc_rf.deserialize_json(
            data["drcRf"]
        )
    if "lfeControl" in data:
        import aws_sdk_medialive.types.eac3_lfe_control

        out["lfe_control"] = aws_sdk_medialive.types.eac3_lfe_control.deserialize_json(
            data["lfeControl"]
        )
    if "lfeFilter" in data:
        import aws_sdk_medialive.types.eac3_lfe_filter

        out["lfe_filter"] = aws_sdk_medialive.types.eac3_lfe_filter.deserialize_json(
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
        import aws_sdk_medialive.types.eac3_metadata_control

        out["metadata_control"] = (
            aws_sdk_medialive.types.eac3_metadata_control.deserialize_json(
                data["metadataControl"]
            )
        )
    if "passthroughControl" in data:
        import aws_sdk_medialive.types.eac3_passthrough_control

        out["passthrough_control"] = (
            aws_sdk_medialive.types.eac3_passthrough_control.deserialize_json(
                data["passthroughControl"]
            )
        )
    if "phaseControl" in data:
        import aws_sdk_medialive.types.eac3_phase_control

        out["phase_control"] = (
            aws_sdk_medialive.types.eac3_phase_control.deserialize_json(
                data["phaseControl"]
            )
        )
    if "stereoDownmix" in data:
        import aws_sdk_medialive.types.eac3_stereo_downmix

        out["stereo_downmix"] = (
            aws_sdk_medialive.types.eac3_stereo_downmix.deserialize_json(
                data["stereoDownmix"]
            )
        )
    if "surroundExMode" in data:
        import aws_sdk_medialive.types.eac3_surround_ex_mode

        out["surround_ex_mode"] = (
            aws_sdk_medialive.types.eac3_surround_ex_mode.deserialize_json(
                data["surroundExMode"]
            )
        )
    if "surroundMode" in data:
        import aws_sdk_medialive.types.eac3_surround_mode

        out["surround_mode"] = (
            aws_sdk_medialive.types.eac3_surround_mode.deserialize_json(
                data["surroundMode"]
            )
        )
    return out
