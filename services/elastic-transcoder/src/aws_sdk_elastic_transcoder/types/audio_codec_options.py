"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#AudioCodecOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.audio_bit_depth
    import aws_sdk_elastic_transcoder.types.audio_bit_order
    import aws_sdk_elastic_transcoder.types.audio_codec_profile
    import aws_sdk_elastic_transcoder.types.audio_signed


class AudioCodecOptions(TypedDict):
    profile: NotRequired[
        "aws_sdk_elastic_transcoder.types.audio_codec_profile.AudioCodecProfile"
    ]
    """<p>You can only choose an audio profile when you specify AAC for the value of Audio:Codec.</p> <p>Specify the AAC profile for the output file. Elastic Transcoder supports the following profiles:</p> <ul> <li> <p> <code>auto</code>: If you specify <code>auto</code>, Elastic Transcoder selects the profile based on the bit rate selected for the output file.</p> </li> <li> <p> <code>AAC-LC</code>: The most common AAC profile. Use for bit rates larger than 64 kbps.</p> </li> <li> <p> <code>HE-AAC</code>: Not supported on some older players and devices. Use for bit rates between 40 and 80 kbps.</p> </li> <li> <p> <code>HE-AACv2</code>: Not supported on some players and devices. Use for bit rates less than 48 kbps.</p> </li> </ul> <p>All outputs in a <code>Smooth</code> playlist must have the same value for <code>Profile</code>.</p> <note> <p>If you created any presets before AAC profiles were added, Elastic Transcoder automatically updated your presets to use AAC-LC. You can change the value as required.</p> </note>"""
    bit_depth: NotRequired[
        "aws_sdk_elastic_transcoder.types.audio_bit_depth.AudioBitDepth"
    ]
    """<p>You can only choose an audio bit depth when you specify <code>flac</code> or <code>pcm</code> for the value of Audio:Codec.</p> <p>The bit depth of a sample is how many bits of information are included in the audio samples. The higher the bit depth, the better the audio, but the larger the file.</p> <p>Valid values are <code>16</code> and <code>24</code>.</p> <p>The most common bit depth is <code>24</code>.</p>"""
    bit_order: NotRequired[
        "aws_sdk_elastic_transcoder.types.audio_bit_order.AudioBitOrder"
    ]
    """<p>You can only choose an audio bit order when you specify <code>pcm</code> for the value of Audio:Codec.</p> <p>The order the bits of a PCM sample are stored in.</p> <p>The supported value is <code>LittleEndian</code>.</p>"""
    signed: NotRequired["aws_sdk_elastic_transcoder.types.audio_signed.AudioSigned"]
    """<p>You can only choose whether an audio sample is signed when you specify <code>pcm</code> for the value of Audio:Codec.</p> <p>Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned).</p> <p>The supported value is <code>Signed</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioCodecOptions) -> dict:
    out: dict = {}
    if "profile" in value:
        out["Profile"] = value["profile"]
    if "bit_depth" in value:
        out["BitDepth"] = value["bit_depth"]
    if "bit_order" in value:
        out["BitOrder"] = value["bit_order"]
    if "signed" in value:
        out["Signed"] = value["signed"]
    return out


def deserialize_json(data: dict) -> AudioCodecOptions:
    out: AudioCodecOptions = {}  # type: ignore[typeddict-item]
    if "Profile" in data:
        out["profile"] = data["Profile"]
    if "BitDepth" in data:
        out["bit_depth"] = data["BitDepth"]
    if "BitOrder" in data:
        out["bit_order"] = data["BitOrder"]
    if "Signed" in data:
        out["signed"] = data["Signed"]
    return out
