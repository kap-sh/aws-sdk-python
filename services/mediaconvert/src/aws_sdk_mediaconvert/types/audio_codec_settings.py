"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioCodecSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.aac_settings
    import aws_sdk_mediaconvert.types.ac3_settings
    import aws_sdk_mediaconvert.types.ac4_settings
    import aws_sdk_mediaconvert.types.aiff_settings
    import aws_sdk_mediaconvert.types.audio_codec
    import aws_sdk_mediaconvert.types.eac3_atmos_settings
    import aws_sdk_mediaconvert.types.eac3_settings
    import aws_sdk_mediaconvert.types.flac_settings
    import aws_sdk_mediaconvert.types.mp2_settings
    import aws_sdk_mediaconvert.types.mp3_settings
    import aws_sdk_mediaconvert.types.opus_settings
    import aws_sdk_mediaconvert.types.vorbis_settings
    import aws_sdk_mediaconvert.types.wav_settings


class AudioCodecSettings(TypedDict):
    aac_settings: NotRequired["aws_sdk_mediaconvert.types.aac_settings.AacSettings"]
    """Required when you set Codec to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode to \"VBR\" or \"CBR\". In VBR mode, you control the audio quality with the setting VBR quality. In CBR mode, you use the setting Bitrate. Defaults and valid values depend on the rate control mode."""
    ac3_settings: NotRequired["aws_sdk_mediaconvert.types.ac3_settings.Ac3Settings"]
    """Required when you set Codec to the value AC3."""
    ac4_settings: NotRequired["aws_sdk_mediaconvert.types.ac4_settings.Ac4Settings"]
    """Required when you set Codec to the value AC4."""
    aiff_settings: NotRequired["aws_sdk_mediaconvert.types.aiff_settings.AiffSettings"]
    """Required when you set Codec to the value AIFF."""
    codec: NotRequired["aws_sdk_mediaconvert.types.audio_codec.AudioCodec"]
    """Choose the audio codec for this output. Note that the option Dolby Digital passthrough applies only to Dolby Digital and Dolby Digital Plus audio inputs. Make sure that you choose a codec that's supported with your output container: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#reference-codecs-containers-output-audio For audio-only outputs, make sure that both your input audio codec and your output audio codec are supported for audio-only workflows. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html#reference-codecs-containers-input-audio-only and https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#audio-only-output"""
    eac3_atmos_settings: NotRequired[
        "aws_sdk_mediaconvert.types.eac3_atmos_settings.Eac3AtmosSettings"
    ]
    """Required when you set Codec to the value EAC3_ATMOS."""
    eac3_settings: NotRequired["aws_sdk_mediaconvert.types.eac3_settings.Eac3Settings"]
    """Required when you set Codec to the value EAC3."""
    flac_settings: NotRequired["aws_sdk_mediaconvert.types.flac_settings.FlacSettings"]
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to the value FLAC."""
    mp2_settings: NotRequired["aws_sdk_mediaconvert.types.mp2_settings.Mp2Settings"]
    """Required when you set Codec to the value MP2."""
    mp3_settings: NotRequired["aws_sdk_mediaconvert.types.mp3_settings.Mp3Settings"]
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to the value MP3."""
    opus_settings: NotRequired["aws_sdk_mediaconvert.types.opus_settings.OpusSettings"]
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to the value OPUS."""
    vorbis_settings: NotRequired[
        "aws_sdk_mediaconvert.types.vorbis_settings.VorbisSettings"
    ]
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to the value Vorbis."""
    wav_settings: NotRequired["aws_sdk_mediaconvert.types.wav_settings.WavSettings"]
    """Required when you set Codec to the value WAV."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioCodecSettings) -> dict:
    out: dict = {}
    if "aac_settings" in value:
        import aws_sdk_mediaconvert.types.aac_settings

        out["aacSettings"] = aws_sdk_mediaconvert.types.aac_settings.serialize_json(
            value["aac_settings"]
        )
    if "ac3_settings" in value:
        import aws_sdk_mediaconvert.types.ac3_settings

        out["ac3Settings"] = aws_sdk_mediaconvert.types.ac3_settings.serialize_json(
            value["ac3_settings"]
        )
    if "ac4_settings" in value:
        import aws_sdk_mediaconvert.types.ac4_settings

        out["ac4Settings"] = aws_sdk_mediaconvert.types.ac4_settings.serialize_json(
            value["ac4_settings"]
        )
    if "aiff_settings" in value:
        import aws_sdk_mediaconvert.types.aiff_settings

        out["aiffSettings"] = aws_sdk_mediaconvert.types.aiff_settings.serialize_json(
            value["aiff_settings"]
        )
    if "codec" in value:
        import aws_sdk_mediaconvert.types.audio_codec

        out["codec"] = aws_sdk_mediaconvert.types.audio_codec.serialize_json(
            value["codec"]
        )
    if "eac3_atmos_settings" in value:
        import aws_sdk_mediaconvert.types.eac3_atmos_settings

        out["eac3AtmosSettings"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_settings.serialize_json(
                value["eac3_atmos_settings"]
            )
        )
    if "eac3_settings" in value:
        import aws_sdk_mediaconvert.types.eac3_settings

        out["eac3Settings"] = aws_sdk_mediaconvert.types.eac3_settings.serialize_json(
            value["eac3_settings"]
        )
    if "flac_settings" in value:
        import aws_sdk_mediaconvert.types.flac_settings

        out["flacSettings"] = aws_sdk_mediaconvert.types.flac_settings.serialize_json(
            value["flac_settings"]
        )
    if "mp2_settings" in value:
        import aws_sdk_mediaconvert.types.mp2_settings

        out["mp2Settings"] = aws_sdk_mediaconvert.types.mp2_settings.serialize_json(
            value["mp2_settings"]
        )
    if "mp3_settings" in value:
        import aws_sdk_mediaconvert.types.mp3_settings

        out["mp3Settings"] = aws_sdk_mediaconvert.types.mp3_settings.serialize_json(
            value["mp3_settings"]
        )
    if "opus_settings" in value:
        import aws_sdk_mediaconvert.types.opus_settings

        out["opusSettings"] = aws_sdk_mediaconvert.types.opus_settings.serialize_json(
            value["opus_settings"]
        )
    if "vorbis_settings" in value:
        import aws_sdk_mediaconvert.types.vorbis_settings

        out["vorbisSettings"] = (
            aws_sdk_mediaconvert.types.vorbis_settings.serialize_json(
                value["vorbis_settings"]
            )
        )
    if "wav_settings" in value:
        import aws_sdk_mediaconvert.types.wav_settings

        out["wavSettings"] = aws_sdk_mediaconvert.types.wav_settings.serialize_json(
            value["wav_settings"]
        )
    return out


def deserialize_json(data: dict) -> AudioCodecSettings:
    out: AudioCodecSettings = {}  # type: ignore[typeddict-item]
    if "aacSettings" in data:
        import aws_sdk_mediaconvert.types.aac_settings

        out["aac_settings"] = aws_sdk_mediaconvert.types.aac_settings.deserialize_json(
            data["aacSettings"]
        )
    if "ac3Settings" in data:
        import aws_sdk_mediaconvert.types.ac3_settings

        out["ac3_settings"] = aws_sdk_mediaconvert.types.ac3_settings.deserialize_json(
            data["ac3Settings"]
        )
    if "ac4Settings" in data:
        import aws_sdk_mediaconvert.types.ac4_settings

        out["ac4_settings"] = aws_sdk_mediaconvert.types.ac4_settings.deserialize_json(
            data["ac4Settings"]
        )
    if "aiffSettings" in data:
        import aws_sdk_mediaconvert.types.aiff_settings

        out["aiff_settings"] = (
            aws_sdk_mediaconvert.types.aiff_settings.deserialize_json(
                data["aiffSettings"]
            )
        )
    if "codec" in data:
        import aws_sdk_mediaconvert.types.audio_codec

        out["codec"] = aws_sdk_mediaconvert.types.audio_codec.deserialize_json(
            data["codec"]
        )
    if "eac3AtmosSettings" in data:
        import aws_sdk_mediaconvert.types.eac3_atmos_settings

        out["eac3_atmos_settings"] = (
            aws_sdk_mediaconvert.types.eac3_atmos_settings.deserialize_json(
                data["eac3AtmosSettings"]
            )
        )
    if "eac3Settings" in data:
        import aws_sdk_mediaconvert.types.eac3_settings

        out["eac3_settings"] = (
            aws_sdk_mediaconvert.types.eac3_settings.deserialize_json(
                data["eac3Settings"]
            )
        )
    if "flacSettings" in data:
        import aws_sdk_mediaconvert.types.flac_settings

        out["flac_settings"] = (
            aws_sdk_mediaconvert.types.flac_settings.deserialize_json(
                data["flacSettings"]
            )
        )
    if "mp2Settings" in data:
        import aws_sdk_mediaconvert.types.mp2_settings

        out["mp2_settings"] = aws_sdk_mediaconvert.types.mp2_settings.deserialize_json(
            data["mp2Settings"]
        )
    if "mp3Settings" in data:
        import aws_sdk_mediaconvert.types.mp3_settings

        out["mp3_settings"] = aws_sdk_mediaconvert.types.mp3_settings.deserialize_json(
            data["mp3Settings"]
        )
    if "opusSettings" in data:
        import aws_sdk_mediaconvert.types.opus_settings

        out["opus_settings"] = (
            aws_sdk_mediaconvert.types.opus_settings.deserialize_json(
                data["opusSettings"]
            )
        )
    if "vorbisSettings" in data:
        import aws_sdk_mediaconvert.types.vorbis_settings

        out["vorbis_settings"] = (
            aws_sdk_mediaconvert.types.vorbis_settings.deserialize_json(
                data["vorbisSettings"]
            )
        )
    if "wavSettings" in data:
        import aws_sdk_mediaconvert.types.wav_settings

        out["wav_settings"] = aws_sdk_mediaconvert.types.wav_settings.deserialize_json(
            data["wavSettings"]
        )
    return out
