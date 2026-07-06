"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#AudioParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.audio_bit_rate
    import aws_sdk_elastic_transcoder.types.audio_channels
    import aws_sdk_elastic_transcoder.types.audio_codec
    import aws_sdk_elastic_transcoder.types.audio_codec_options
    import aws_sdk_elastic_transcoder.types.audio_packing_mode
    import aws_sdk_elastic_transcoder.types.audio_sample_rate


class AudioParameters(TypedDict, closed=True):
    codec: NotRequired["aws_sdk_elastic_transcoder.types.audio_codec.AudioCodec"]
    """<p>The audio codec for the output file. Valid values include <code>aac</code>, <code>flac</code>, <code>mp2</code>, <code>mp3</code>, <code>pcm</code>, and <code>vorbis</code>.</p>"""
    sample_rate: NotRequired[
        "aws_sdk_elastic_transcoder.types.audio_sample_rate.AudioSampleRate"
    ]
    """<p>The sample rate of the audio stream in the output file, in Hertz. Valid values include:</p> <p> <code>auto</code>, <code>22050</code>, <code>32000</code>, <code>44100</code>, <code>48000</code>, <code>96000</code> </p> <p>If you specify <code>auto</code>, Elastic Transcoder automatically detects the sample rate.</p>"""
    bit_rate: NotRequired[
        "aws_sdk_elastic_transcoder.types.audio_bit_rate.AudioBitRate"
    ]
    """<p>The bit rate of the audio stream in the output file, in kilobits/second. Enter an integer between 64 and 320, inclusive.</p>"""
    channels: NotRequired[
        "aws_sdk_elastic_transcoder.types.audio_channels.AudioChannels"
    ]
    """<p>The number of audio channels in the output file. The following values are valid:</p> <p> <code>auto</code>, <code>0</code>, <code>1</code>, <code>2</code> </p> <p>One channel carries the information played by a single speaker. For example, a stereo track with two channels sends one channel to the left speaker, and the other channel to the right speaker. The output channels are organized into tracks. If you want Elastic Transcoder to automatically detect the number of audio channels in the input file and use that value for the output file, select <code>auto</code>.</p> <p>The output of a specific channel value and inputs are as follows:</p> <ul> <li> <p> <code>auto</code> <b> channel specified, with any input:</b> Pass through up to eight input channels.</p> </li> <li> <p> <code>0</code> <b> channels specified, with any input:</b> Audio omitted from the output.</p> </li> <li> <p> <code>1</code> <b> channel specified, with at least one input channel:</b> Mono sound.</p> </li> <li> <p> <code>2</code> <b> channels specified, with any input:</b> Two identical mono channels or stereo. For more information about tracks, see <code>Audio:AudioPackingMode.</code> </p> </li> </ul> <p> For more information about how Elastic Transcoder organizes channels and tracks, see <code>Audio:AudioPackingMode</code>.</p>"""
    audio_packing_mode: NotRequired[
        "aws_sdk_elastic_transcoder.types.audio_packing_mode.AudioPackingMode"
    ]
    """<p>The method of organizing audio channels and tracks. Use <code>Audio:Channels</code> to specify the number of channels in your output, and <code>Audio:AudioPackingMode</code> to specify the number of tracks and their relation to the channels. If you do not specify an <code>Audio:AudioPackingMode</code>, Elastic Transcoder uses <code>SingleTrack</code>.</p> <p>The following values are valid:</p> <p> <code>SingleTrack</code>, <code>OneChannelPerTrack</code>, and <code>OneChannelPerTrackWithMosTo8Tracks</code> </p> <p>When you specify <code>SingleTrack</code>, Elastic Transcoder creates a single track for your output. The track can have up to eight channels. Use <code>SingleTrack</code> for all non-<code>mxf</code> containers.</p> <p>The outputs of <code>SingleTrack</code> for a specific channel value and inputs are as follows:</p> <ul> <li> <p> <code>0</code> <b> channels with any input:</b> Audio omitted from the output</p> </li> <li> <p> <code>1, 2, or auto </code> <b>channels with no audio input:</b> Audio omitted from the output</p> </li> <li> <p> <code>1 </code> <b>channel with any input with audio:</b> One track with one channel, downmixed if necessary</p> </li> <li> <p> <code>2 </code> <b>channels with one track with one channel:</b> One track with two identical channels</p> </li> <li> <p> <code>2 or auto </code> <b>channels with two tracks with one channel each:</b> One track with two channels</p> </li> <li> <p> <code>2 or auto </code> <b>channels with one track with two channels:</b> One track with two channels</p> </li> <li> <p> <code>2 </code> <b>channels with one track with multiple channels:</b> One track with two channels</p> </li> <li> <p> <code>auto </code> <b>channels with one track with one channel:</b> One track with one channel</p> </li> <li> <p> <code>auto </code> <b>channels with one track with multiple channels:</b> One track with multiple channels</p> </li> </ul> <p>When you specify <code>OneChannelPerTrack</code>, Elastic Transcoder creates a new track for every channel in your output. Your output can have up to eight single-channel tracks.</p> <p>The outputs of <code>OneChannelPerTrack</code> for a specific channel value and inputs are as follows:</p> <ul> <li> <p> <code>0 </code> <b>channels with any input:</b> Audio omitted from the output</p> </li> <li> <p> <code>1, 2, or auto </code> <b>channels with no audio input:</b> Audio omitted from the output</p> </li> <li> <p> <code>1 </code> <b>channel with any input with audio:</b> One track with one channel, downmixed if necessary</p> </li> <li> <p> <code>2 </code> <b>channels with one track with one channel:</b> Two tracks with one identical channel each</p> </li> <li> <p> <code>2 or auto </code> <b>channels with two tracks with one channel each:</b> Two tracks with one channel each</p> </li> <li> <p> <code>2 or auto </code> <b>channels with one track with two channels:</b> Two tracks with one channel each</p> </li> <li> <p> <code>2 </code> <b>channels with one track with multiple channels:</b> Two tracks with one channel each</p> </li> <li> <p> <code>auto </code> <b>channels with one track with one channel:</b> One track with one channel</p> </li> <li> <p> <code>auto </code> <b>channels with one track with multiple channels:</b> Up to eight tracks with one channel each</p> </li> </ul> <p>When you specify <code>OneChannelPerTrackWithMosTo8Tracks</code>, Elastic Transcoder creates eight single-channel tracks for your output. All tracks that do not contain audio data from an input channel are MOS, or Mit Out Sound, tracks.</p> <p>The outputs of <code>OneChannelPerTrackWithMosTo8Tracks</code> for a specific channel value and inputs are as follows:</p> <ul> <li> <p> <code>0 </code> <b>channels with any input:</b> Audio omitted from the output</p> </li> <li> <p> <code>1, 2, or auto </code> <b>channels with no audio input:</b> Audio omitted from the output</p> </li> <li> <p> <code>1 </code> <b>channel with any input with audio:</b> One track with one channel, downmixed if necessary, plus six MOS tracks</p> </li> <li> <p> <code>2 </code> <b>channels with one track with one channel:</b> Two tracks with one identical channel each, plus six MOS tracks</p> </li> <li> <p> <code>2 or auto </code> <b>channels with two tracks with one channel each:</b> Two tracks with one channel each, plus six MOS tracks</p> </li> <li> <p> <code>2 or auto </code> <b>channels with one track with two channels:</b> Two tracks with one channel each, plus six MOS tracks</p> </li> <li> <p> <code>2 </code> <b>channels with one track with multiple channels:</b> Two tracks with one channel each, plus six MOS tracks</p> </li> <li> <p> <code>auto </code> <b>channels with one track with one channel:</b> One track with one channel, plus seven MOS tracks</p> </li> <li> <p> <code>auto </code> <b>channels with one track with multiple channels:</b> Up to eight tracks with one channel each, plus MOS tracks until there are eight tracks in all</p> </li> </ul>"""
    codec_options: NotRequired[
        "aws_sdk_elastic_transcoder.types.audio_codec_options.AudioCodecOptions"
    ]
    """<p>If you specified <code>AAC</code> for <code>Audio:Codec</code>, this is the <code>AAC</code> compression profile to use. Valid values include:</p> <p> <code>auto</code>, <code>AAC-LC</code>, <code>HE-AAC</code>, <code>HE-AACv2</code> </p> <p>If you specify <code>auto</code>, Elastic Transcoder chooses a profile based on the bit rate of the output file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioParameters) -> dict:
    out: dict = {}
    if "codec" in value:
        out["Codec"] = value["codec"]
    if "sample_rate" in value:
        out["SampleRate"] = value["sample_rate"]
    if "bit_rate" in value:
        out["BitRate"] = value["bit_rate"]
    if "channels" in value:
        out["Channels"] = value["channels"]
    if "audio_packing_mode" in value:
        out["AudioPackingMode"] = value["audio_packing_mode"]
    if "codec_options" in value:
        import aws_sdk_elastic_transcoder.types.audio_codec_options

        out["CodecOptions"] = (
            aws_sdk_elastic_transcoder.types.audio_codec_options.serialize_json(
                value["codec_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioParameters:
    out: AudioParameters = {}  # type: ignore[typeddict-item]
    if "Codec" in data:
        out["codec"] = data["Codec"]
    if "SampleRate" in data:
        out["sample_rate"] = data["SampleRate"]
    if "BitRate" in data:
        out["bit_rate"] = data["BitRate"]
    if "Channels" in data:
        out["channels"] = data["Channels"]
    if "AudioPackingMode" in data:
        out["audio_packing_mode"] = data["AudioPackingMode"]
    if "CodecOptions" in data:
        import aws_sdk_elastic_transcoder.types.audio_codec_options

        out["codec_options"] = (
            aws_sdk_elastic_transcoder.types.audio_codec_options.deserialize_json(
                data["CodecOptions"]
            )
        )
    return out
