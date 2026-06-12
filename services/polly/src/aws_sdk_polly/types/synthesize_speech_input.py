"""Generated from Smithy shape ``com.amazonaws.polly#SynthesizeSpeechInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_polly.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_polly.types.engine
    import aws_sdk_polly.types.language_code
    import aws_sdk_polly.types.lexicon_name_list
    import aws_sdk_polly.types.output_format
    import aws_sdk_polly.types.sample_rate
    import aws_sdk_polly.types.speech_mark_type_list
    import aws_sdk_polly.types.text
    import aws_sdk_polly.types.text_type
    import aws_sdk_polly.types.voice_id


class SynthesizeSpeechInput(TypedDict):
    engine: NotRequired["aws_sdk_polly.types.engine.Engine"]
    """<p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code>, or <code>generative</code>) for Amazon Polly to use when processing input text for speech synthesis. Provide an engine that is supported by the voice you select. If you don't provide an engine, the standard engine is selected by default. If a chosen voice isn't supported by the standard engine, this will result in an error. For information on Amazon Polly voices and which voices are available for each engine, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/voicelist.html\">Available Voices</a>.</p>"""
    language_code: NotRequired["aws_sdk_polly.types.language_code.LanguageCode"]
    """<p>Optional language code for the Synthesize Speech request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). </p> <p>If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the <a href=\"https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html\">DescribeVoices</a> operation for the <code>LanguageCode</code> parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.</p>"""
    lexicon_names: NotRequired["aws_sdk_polly.types.lexicon_name_list.LexiconNameList"]
    """<p>List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html\">PutLexicon</a>.</p>"""
    output_format: "aws_sdk_polly.types.output_format.OutputFormat"
    """<p> The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, ogg_opus, mu-law, a-law or pcm. For speech marks, this will be json. </p> <p>When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format. </p>"""
    sample_rate: NotRequired["aws_sdk_polly.types.sample_rate.SampleRate"]
    """<p>The audio frequency specified in Hz.</p> <p>The valid values for mp3 and ogg_vorbis are \"8000\", \"16000\", \"22050\", \"24000\", \"44100\" and \"48000\". The default value for standard voices is \"22050\". The default value for neural voices is \"24000\". The default value for long-form voices is \"24000\". The default value for generative voices is \"24000\".</p> <p>Valid values for pcm are \"8000\" and \"16000\" The default value is \"16000\". </p> <p>Valid value for ogg_opus is \"48000\". </p> <p>Valid value for mu-law and a-law is \"8000\". </p>"""
    speech_mark_types: NotRequired[
        "aws_sdk_polly.types.speech_mark_type_list.SpeechMarkTypeList"
    ]
    """<p>The type of speech marks returned for the input text.</p>"""
    text: "aws_sdk_polly.types.text.Text"
    """<p> Input text to synthesize. If you specify <code>ssml</code> as the <code>TextType</code>, follow the SSML format for the input text. </p>"""
    text_type: NotRequired["aws_sdk_polly.types.text_type.TextType"]
    """<p> Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/ssml.html\">Using SSML</a>.</p>"""
    voice_id: "aws_sdk_polly.types.voice_id.VoiceId"
    """<p> Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the <a href=\"https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html\">DescribeVoices</a> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SynthesizeSpeechInput) -> dict:
    out: dict = {}
    if "engine" in value:
        import aws_sdk_polly.types.engine

        out["Engine"] = aws_sdk_polly.types.engine.serialize_json(value["engine"])
    if "language_code" in value:
        import aws_sdk_polly.types.language_code

        out["LanguageCode"] = aws_sdk_polly.types.language_code.serialize_json(
            value["language_code"]
        )
    if "lexicon_names" in value:
        import aws_sdk_polly.types.lexicon_name_list

        out["LexiconNames"] = aws_sdk_polly.types.lexicon_name_list.serialize_json(
            value["lexicon_names"]
        )
    import aws_sdk_polly.types.output_format

    out["OutputFormat"] = aws_sdk_polly.types.output_format.serialize_json(
        value["output_format"]
    )
    if "sample_rate" in value:
        out["SampleRate"] = value["sample_rate"]
    if "speech_mark_types" in value:
        import aws_sdk_polly.types.speech_mark_type_list

        out["SpeechMarkTypes"] = (
            aws_sdk_polly.types.speech_mark_type_list.serialize_json(
                value["speech_mark_types"]
            )
        )
    out["Text"] = value["text"]
    if "text_type" in value:
        import aws_sdk_polly.types.text_type

        out["TextType"] = aws_sdk_polly.types.text_type.serialize_json(
            value["text_type"]
        )
    import aws_sdk_polly.types.voice_id

    out["VoiceId"] = aws_sdk_polly.types.voice_id.serialize_json(value["voice_id"])
    return out


def deserialize_json(data: dict) -> SynthesizeSpeechInput:
    out: SynthesizeSpeechInput = {}  # type: ignore[typeddict-item]
    if "Engine" in data:
        import aws_sdk_polly.types.engine

        out["engine"] = aws_sdk_polly.types.engine.deserialize_json(data["Engine"])
    if "LanguageCode" in data:
        import aws_sdk_polly.types.language_code

        out["language_code"] = aws_sdk_polly.types.language_code.deserialize_json(
            data["LanguageCode"]
        )
    if "LexiconNames" in data:
        import aws_sdk_polly.types.lexicon_name_list

        out["lexicon_names"] = aws_sdk_polly.types.lexicon_name_list.deserialize_json(
            data["LexiconNames"]
        )
    if "OutputFormat" in data:
        import aws_sdk_polly.types.output_format

        out["output_format"] = aws_sdk_polly.types.output_format.deserialize_json(
            data["OutputFormat"]
        )
    else:
        raise DeserializationError("SynthesizeSpeechInput.output_format required")
    if "SampleRate" in data:
        out["sample_rate"] = data["SampleRate"]
    if "SpeechMarkTypes" in data:
        import aws_sdk_polly.types.speech_mark_type_list

        out["speech_mark_types"] = (
            aws_sdk_polly.types.speech_mark_type_list.deserialize_json(
                data["SpeechMarkTypes"]
            )
        )
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("SynthesizeSpeechInput.text required")
    if "TextType" in data:
        import aws_sdk_polly.types.text_type

        out["text_type"] = aws_sdk_polly.types.text_type.deserialize_json(
            data["TextType"]
        )
    if "VoiceId" in data:
        import aws_sdk_polly.types.voice_id

        out["voice_id"] = aws_sdk_polly.types.voice_id.deserialize_json(data["VoiceId"])
    else:
        raise DeserializationError("SynthesizeSpeechInput.voice_id required")
    return out
