"""Generated from Smithy shape ``com.amazonaws.medialive#AudioCodecSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.aac_settings
    import aws_sdk_medialive.types.ac3_settings
    import aws_sdk_medialive.types.eac3_atmos_settings
    import aws_sdk_medialive.types.eac3_settings
    import aws_sdk_medialive.types.mp2_settings
    import aws_sdk_medialive.types.pass_through_settings
    import aws_sdk_medialive.types.wav_settings


class AudioCodecSettings(TypedDict):
    aac_settings: NotRequired["aws_sdk_medialive.types.aac_settings.AacSettings"]
    ac3_settings: NotRequired["aws_sdk_medialive.types.ac3_settings.Ac3Settings"]
    eac3_atmos_settings: NotRequired[
        "aws_sdk_medialive.types.eac3_atmos_settings.Eac3AtmosSettings"
    ]
    eac3_settings: NotRequired["aws_sdk_medialive.types.eac3_settings.Eac3Settings"]
    mp2_settings: NotRequired["aws_sdk_medialive.types.mp2_settings.Mp2Settings"]
    pass_through_settings: NotRequired[
        "aws_sdk_medialive.types.pass_through_settings.PassThroughSettings"
    ]
    wav_settings: NotRequired["aws_sdk_medialive.types.wav_settings.WavSettings"]


# --- restJson1 ser/de ---
def serialize_json(value: AudioCodecSettings) -> dict:
    out: dict = {}
    if "aac_settings" in value:
        import aws_sdk_medialive.types.aac_settings

        out["aacSettings"] = aws_sdk_medialive.types.aac_settings.serialize_json(
            value["aac_settings"]
        )
    if "ac3_settings" in value:
        import aws_sdk_medialive.types.ac3_settings

        out["ac3Settings"] = aws_sdk_medialive.types.ac3_settings.serialize_json(
            value["ac3_settings"]
        )
    if "eac3_atmos_settings" in value:
        import aws_sdk_medialive.types.eac3_atmos_settings

        out["eac3AtmosSettings"] = (
            aws_sdk_medialive.types.eac3_atmos_settings.serialize_json(
                value["eac3_atmos_settings"]
            )
        )
    if "eac3_settings" in value:
        import aws_sdk_medialive.types.eac3_settings

        out["eac3Settings"] = aws_sdk_medialive.types.eac3_settings.serialize_json(
            value["eac3_settings"]
        )
    if "mp2_settings" in value:
        import aws_sdk_medialive.types.mp2_settings

        out["mp2Settings"] = aws_sdk_medialive.types.mp2_settings.serialize_json(
            value["mp2_settings"]
        )
    if "pass_through_settings" in value:
        import aws_sdk_medialive.types.pass_through_settings

        out["passThroughSettings"] = (
            aws_sdk_medialive.types.pass_through_settings.serialize_json(
                value["pass_through_settings"]
            )
        )
    if "wav_settings" in value:
        import aws_sdk_medialive.types.wav_settings

        out["wavSettings"] = aws_sdk_medialive.types.wav_settings.serialize_json(
            value["wav_settings"]
        )
    return out


def deserialize_json(data: dict) -> AudioCodecSettings:
    out: AudioCodecSettings = {}  # type: ignore[typeddict-item]
    if "aacSettings" in data:
        import aws_sdk_medialive.types.aac_settings

        out["aac_settings"] = aws_sdk_medialive.types.aac_settings.deserialize_json(
            data["aacSettings"]
        )
    if "ac3Settings" in data:
        import aws_sdk_medialive.types.ac3_settings

        out["ac3_settings"] = aws_sdk_medialive.types.ac3_settings.deserialize_json(
            data["ac3Settings"]
        )
    if "eac3AtmosSettings" in data:
        import aws_sdk_medialive.types.eac3_atmos_settings

        out["eac3_atmos_settings"] = (
            aws_sdk_medialive.types.eac3_atmos_settings.deserialize_json(
                data["eac3AtmosSettings"]
            )
        )
    if "eac3Settings" in data:
        import aws_sdk_medialive.types.eac3_settings

        out["eac3_settings"] = aws_sdk_medialive.types.eac3_settings.deserialize_json(
            data["eac3Settings"]
        )
    if "mp2Settings" in data:
        import aws_sdk_medialive.types.mp2_settings

        out["mp2_settings"] = aws_sdk_medialive.types.mp2_settings.deserialize_json(
            data["mp2Settings"]
        )
    if "passThroughSettings" in data:
        import aws_sdk_medialive.types.pass_through_settings

        out["pass_through_settings"] = (
            aws_sdk_medialive.types.pass_through_settings.deserialize_json(
                data["passThroughSettings"]
            )
        )
    if "wavSettings" in data:
        import aws_sdk_medialive.types.wav_settings

        out["wav_settings"] = aws_sdk_medialive.types.wav_settings.deserialize_json(
            data["wavSettings"]
        )
    return out
