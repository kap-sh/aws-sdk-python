"""Generated from Smithy shape ``com.amazonaws.medialive#AudioCodecSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.aac_settings
    import capo_medialive.types.ac3_settings
    import capo_medialive.types.eac3_atmos_settings
    import capo_medialive.types.eac3_settings
    import capo_medialive.types.mp2_settings
    import capo_medialive.types.pass_through_settings
    import capo_medialive.types.wav_settings


class AudioCodecSettings(TypedDict, closed=True):
    aac_settings: NotRequired["capo_medialive.types.aac_settings.AacSettings"]
    ac3_settings: NotRequired["capo_medialive.types.ac3_settings.Ac3Settings"]
    eac3_atmos_settings: NotRequired[
        "capo_medialive.types.eac3_atmos_settings.Eac3AtmosSettings"
    ]
    eac3_settings: NotRequired["capo_medialive.types.eac3_settings.Eac3Settings"]
    mp2_settings: NotRequired["capo_medialive.types.mp2_settings.Mp2Settings"]
    pass_through_settings: NotRequired[
        "capo_medialive.types.pass_through_settings.PassThroughSettings"
    ]
    wav_settings: NotRequired["capo_medialive.types.wav_settings.WavSettings"]


# --- restJson1 ser/de ---
def serialize_json(value: AudioCodecSettings) -> dict:
    out: dict = {}
    if "aac_settings" in value:
        import capo_medialive.types.aac_settings

        out["aacSettings"] = capo_medialive.types.aac_settings.serialize_json(
            value["aac_settings"]
        )
    if "ac3_settings" in value:
        import capo_medialive.types.ac3_settings

        out["ac3Settings"] = capo_medialive.types.ac3_settings.serialize_json(
            value["ac3_settings"]
        )
    if "eac3_atmos_settings" in value:
        import capo_medialive.types.eac3_atmos_settings

        out["eac3AtmosSettings"] = (
            capo_medialive.types.eac3_atmos_settings.serialize_json(
                value["eac3_atmos_settings"]
            )
        )
    if "eac3_settings" in value:
        import capo_medialive.types.eac3_settings

        out["eac3Settings"] = capo_medialive.types.eac3_settings.serialize_json(
            value["eac3_settings"]
        )
    if "mp2_settings" in value:
        import capo_medialive.types.mp2_settings

        out["mp2Settings"] = capo_medialive.types.mp2_settings.serialize_json(
            value["mp2_settings"]
        )
    if "pass_through_settings" in value:
        import capo_medialive.types.pass_through_settings

        out["passThroughSettings"] = (
            capo_medialive.types.pass_through_settings.serialize_json(
                value["pass_through_settings"]
            )
        )
    if "wav_settings" in value:
        import capo_medialive.types.wav_settings

        out["wavSettings"] = capo_medialive.types.wav_settings.serialize_json(
            value["wav_settings"]
        )
    return out


def deserialize_json(data: dict) -> AudioCodecSettings:
    out: AudioCodecSettings = {}  # type: ignore[typeddict-item]
    if "aacSettings" in data:
        import capo_medialive.types.aac_settings

        out["aac_settings"] = capo_medialive.types.aac_settings.deserialize_json(
            data["aacSettings"]
        )
    if "ac3Settings" in data:
        import capo_medialive.types.ac3_settings

        out["ac3_settings"] = capo_medialive.types.ac3_settings.deserialize_json(
            data["ac3Settings"]
        )
    if "eac3AtmosSettings" in data:
        import capo_medialive.types.eac3_atmos_settings

        out["eac3_atmos_settings"] = (
            capo_medialive.types.eac3_atmos_settings.deserialize_json(
                data["eac3AtmosSettings"]
            )
        )
    if "eac3Settings" in data:
        import capo_medialive.types.eac3_settings

        out["eac3_settings"] = capo_medialive.types.eac3_settings.deserialize_json(
            data["eac3Settings"]
        )
    if "mp2Settings" in data:
        import capo_medialive.types.mp2_settings

        out["mp2_settings"] = capo_medialive.types.mp2_settings.deserialize_json(
            data["mp2Settings"]
        )
    if "passThroughSettings" in data:
        import capo_medialive.types.pass_through_settings

        out["pass_through_settings"] = (
            capo_medialive.types.pass_through_settings.deserialize_json(
                data["passThroughSettings"]
            )
        )
    if "wavSettings" in data:
        import capo_medialive.types.wav_settings

        out["wav_settings"] = capo_medialive.types.wav_settings.deserialize_json(
            data["wavSettings"]
        )
    return out
