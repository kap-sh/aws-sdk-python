"""Generated from Smithy shape ``com.amazonaws.medialive#AacSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.aac_coding_mode
    import aws_sdk_medialive.types.aac_input_type
    import aws_sdk_medialive.types.aac_profile
    import aws_sdk_medialive.types.aac_rate_control_mode
    import aws_sdk_medialive.types.aac_raw_format
    import aws_sdk_medialive.types.aac_spec
    import aws_sdk_medialive.types.aac_vbr_quality


class AacSettings(TypedDict):
    bitrate: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Average bitrate in bits/second. Valid values depend on rate control mode and profile."""
    coding_mode: NotRequired["aws_sdk_medialive.types.aac_coding_mode.AacCodingMode"]
    """Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. The adReceiverMix setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E."""
    input_type: NotRequired["aws_sdk_medialive.types.aac_input_type.AacInputType"]
    r"""Set to \"broadcasterMixedAd\" when input contains pre-mixed main audio + AD (narration) as a stereo pair. The Audio Type field (audioType) will be set to 3, which signals to downstream systems that this stream contains \"broadcaster mixed AD\". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. The values in audioTypeControl and audioType (in AudioDescription) are ignored when set to broadcasterMixedAd. Leave set to \"normal\" when input does not contain pre-mixed audio + AD."""
    profile: NotRequired["aws_sdk_medialive.types.aac_profile.AacProfile"]
    """AAC Profile."""
    rate_control_mode: NotRequired[
        "aws_sdk_medialive.types.aac_rate_control_mode.AacRateControlMode"
    ]
    """Rate Control Mode."""
    raw_format: NotRequired["aws_sdk_medialive.types.aac_raw_format.AacRawFormat"]
    """Sets LATM / LOAS AAC output for raw containers."""
    sample_rate: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Sample rate in Hz. Valid values depend on rate control mode and profile."""
    spec: NotRequired["aws_sdk_medialive.types.aac_spec.AacSpec"]
    """Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers."""
    vbr_quality: NotRequired["aws_sdk_medialive.types.aac_vbr_quality.AacVbrQuality"]
    """VBR Quality Level - Only used if rateControlMode is VBR."""


# --- restJson1 ser/de ---
def serialize_json(value: AacSettings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "coding_mode" in value:
        import aws_sdk_medialive.types.aac_coding_mode

        out["codingMode"] = aws_sdk_medialive.types.aac_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "input_type" in value:
        import aws_sdk_medialive.types.aac_input_type

        out["inputType"] = aws_sdk_medialive.types.aac_input_type.serialize_json(
            value["input_type"]
        )
    if "profile" in value:
        import aws_sdk_medialive.types.aac_profile

        out["profile"] = aws_sdk_medialive.types.aac_profile.serialize_json(
            value["profile"]
        )
    if "rate_control_mode" in value:
        import aws_sdk_medialive.types.aac_rate_control_mode

        out["rateControlMode"] = (
            aws_sdk_medialive.types.aac_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "raw_format" in value:
        import aws_sdk_medialive.types.aac_raw_format

        out["rawFormat"] = aws_sdk_medialive.types.aac_raw_format.serialize_json(
            value["raw_format"]
        )
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "spec" in value:
        import aws_sdk_medialive.types.aac_spec

        out["spec"] = aws_sdk_medialive.types.aac_spec.serialize_json(value["spec"])
    if "vbr_quality" in value:
        import aws_sdk_medialive.types.aac_vbr_quality

        out["vbrQuality"] = aws_sdk_medialive.types.aac_vbr_quality.serialize_json(
            value["vbr_quality"]
        )
    return out


def deserialize_json(data: dict) -> AacSettings:
    out: AacSettings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "codingMode" in data:
        import aws_sdk_medialive.types.aac_coding_mode

        out["coding_mode"] = aws_sdk_medialive.types.aac_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if "inputType" in data:
        import aws_sdk_medialive.types.aac_input_type

        out["input_type"] = aws_sdk_medialive.types.aac_input_type.deserialize_json(
            data["inputType"]
        )
    if "profile" in data:
        import aws_sdk_medialive.types.aac_profile

        out["profile"] = aws_sdk_medialive.types.aac_profile.deserialize_json(
            data["profile"]
        )
    if "rateControlMode" in data:
        import aws_sdk_medialive.types.aac_rate_control_mode

        out["rate_control_mode"] = (
            aws_sdk_medialive.types.aac_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if "rawFormat" in data:
        import aws_sdk_medialive.types.aac_raw_format

        out["raw_format"] = aws_sdk_medialive.types.aac_raw_format.deserialize_json(
            data["rawFormat"]
        )
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    if "spec" in data:
        import aws_sdk_medialive.types.aac_spec

        out["spec"] = aws_sdk_medialive.types.aac_spec.deserialize_json(data["spec"])
    if "vbrQuality" in data:
        import aws_sdk_medialive.types.aac_vbr_quality

        out["vbr_quality"] = aws_sdk_medialive.types.aac_vbr_quality.deserialize_json(
            data["vbrQuality"]
        )
    return out
