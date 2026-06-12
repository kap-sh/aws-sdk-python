"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3Settings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.__integer_min1_max31
    import aws_sdk_medialive.types.ac3_attenuation_control
    import aws_sdk_medialive.types.ac3_bitstream_mode
    import aws_sdk_medialive.types.ac3_coding_mode
    import aws_sdk_medialive.types.ac3_drc_profile
    import aws_sdk_medialive.types.ac3_lfe_filter
    import aws_sdk_medialive.types.ac3_metadata_control


class Ac3Settings(TypedDict):
    bitrate: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Average bitrate in bits/second. Valid bitrates depend on the coding mode."""
    bitstream_mode: NotRequired[
        "aws_sdk_medialive.types.ac3_bitstream_mode.Ac3BitstreamMode"
    ]
    """Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values."""
    coding_mode: NotRequired["aws_sdk_medialive.types.ac3_coding_mode.Ac3CodingMode"]
    """Dolby Digital coding mode. Determines number of channels."""
    dialnorm: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max31.__integerMin1Max31"
    ]
    """Sets the dialnorm for the output. If excluded and input audio is Dolby Digital, dialnorm will be passed through."""
    drc_profile: NotRequired["aws_sdk_medialive.types.ac3_drc_profile.Ac3DrcProfile"]
    """If set to filmStandard, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification."""
    lfe_filter: NotRequired["aws_sdk_medialive.types.ac3_lfe_filter.Ac3LfeFilter"]
    """When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid in codingMode32Lfe mode."""
    metadata_control: NotRequired[
        "aws_sdk_medialive.types.ac3_metadata_control.Ac3MetadataControl"
    ]
    """When set to \"followInput\", encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used."""
    attenuation_control: NotRequired[
        "aws_sdk_medialive.types.ac3_attenuation_control.Ac3AttenuationControl"
    ]
    """Applies a 3 dB attenuation to the surround channels. Applies only when the coding mode parameter is CODING_MODE_3_2_LFE."""


# --- restJson1 ser/de ---
def serialize_json(value: Ac3Settings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "bitstream_mode" in value:
        import aws_sdk_medialive.types.ac3_bitstream_mode

        out["bitstreamMode"] = (
            aws_sdk_medialive.types.ac3_bitstream_mode.serialize_json(
                value["bitstream_mode"]
            )
        )
    if "coding_mode" in value:
        import aws_sdk_medialive.types.ac3_coding_mode

        out["codingMode"] = aws_sdk_medialive.types.ac3_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "dialnorm" in value:
        out["dialnorm"] = value["dialnorm"]
    if "drc_profile" in value:
        import aws_sdk_medialive.types.ac3_drc_profile

        out["drcProfile"] = aws_sdk_medialive.types.ac3_drc_profile.serialize_json(
            value["drc_profile"]
        )
    if "lfe_filter" in value:
        import aws_sdk_medialive.types.ac3_lfe_filter

        out["lfeFilter"] = aws_sdk_medialive.types.ac3_lfe_filter.serialize_json(
            value["lfe_filter"]
        )
    if "metadata_control" in value:
        import aws_sdk_medialive.types.ac3_metadata_control

        out["metadataControl"] = (
            aws_sdk_medialive.types.ac3_metadata_control.serialize_json(
                value["metadata_control"]
            )
        )
    if "attenuation_control" in value:
        import aws_sdk_medialive.types.ac3_attenuation_control

        out["attenuationControl"] = (
            aws_sdk_medialive.types.ac3_attenuation_control.serialize_json(
                value["attenuation_control"]
            )
        )
    return out


def deserialize_json(data: dict) -> Ac3Settings:
    out: Ac3Settings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "bitstreamMode" in data:
        import aws_sdk_medialive.types.ac3_bitstream_mode

        out["bitstream_mode"] = (
            aws_sdk_medialive.types.ac3_bitstream_mode.deserialize_json(
                data["bitstreamMode"]
            )
        )
    if "codingMode" in data:
        import aws_sdk_medialive.types.ac3_coding_mode

        out["coding_mode"] = aws_sdk_medialive.types.ac3_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if "dialnorm" in data:
        out["dialnorm"] = data["dialnorm"]
    if "drcProfile" in data:
        import aws_sdk_medialive.types.ac3_drc_profile

        out["drc_profile"] = aws_sdk_medialive.types.ac3_drc_profile.deserialize_json(
            data["drcProfile"]
        )
    if "lfeFilter" in data:
        import aws_sdk_medialive.types.ac3_lfe_filter

        out["lfe_filter"] = aws_sdk_medialive.types.ac3_lfe_filter.deserialize_json(
            data["lfeFilter"]
        )
    if "metadataControl" in data:
        import aws_sdk_medialive.types.ac3_metadata_control

        out["metadata_control"] = (
            aws_sdk_medialive.types.ac3_metadata_control.deserialize_json(
                data["metadataControl"]
            )
        )
    if "attenuationControl" in data:
        import aws_sdk_medialive.types.ac3_attenuation_control

        out["attenuation_control"] = (
            aws_sdk_medialive.types.ac3_attenuation_control.deserialize_json(
                data["attenuationControl"]
            )
        )
    return out
