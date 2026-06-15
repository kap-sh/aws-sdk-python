"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_polly.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_polly.types.engine
    import aws_sdk_polly.types.language_code
    import aws_sdk_polly.types.lexicon_name_list
    import aws_sdk_polly.types.output_format
    import aws_sdk_polly.types.output_s3_bucket_name
    import aws_sdk_polly.types.output_s3_key_prefix
    import aws_sdk_polly.types.sample_rate
    import aws_sdk_polly.types.sns_topic_arn
    import aws_sdk_polly.types.speech_mark_type_list
    import aws_sdk_polly.types.text
    import aws_sdk_polly.types.text_type
    import aws_sdk_polly.types.voice_id


class StartSpeechSynthesisTaskInput(TypedDict):
    engine: NotRequired["aws_sdk_polly.types.engine.Engine"]
    """<p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code> or <code>generative</code>) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.</p>"""
    language_code: NotRequired["aws_sdk_polly.types.language_code.LanguageCode"]
    r"""<p>Optional language code for the Speech Synthesis request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). </p> <p>If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the <a href=\"https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html\">DescribeVoices</a> operation for the <code>LanguageCode</code> parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.</p>"""
    lexicon_names: NotRequired["aws_sdk_polly.types.lexicon_name_list.LexiconNameList"]
    """<p>List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. </p>"""
    output_format: "aws_sdk_polly.types.output_format.OutputFormat"
    """<p>The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, ogg_opus, mu-law, a-law, or pcm. For speech marks, this will be json. </p>"""
    output_s3_bucket_name: (
        "aws_sdk_polly.types.output_s3_bucket_name.OutputS3BucketName"
    )
    """<p>Amazon S3 bucket name to which the output file will be saved.</p>"""
    output_s3_key_prefix: NotRequired[
        "aws_sdk_polly.types.output_s3_key_prefix.OutputS3KeyPrefix"
    ]
    """<p>The Amazon S3 key prefix for the output speech file.</p>"""
    sample_rate: NotRequired["aws_sdk_polly.types.sample_rate.SampleRate"]
    r"""<p>The audio frequency specified in Hz.</p> <p>The valid values for mp3 and ogg_vorbis are \"8000\", \"16000\", \"22050\", and \"24000\". The default value for standard voices is \"22050\". The default value for neural voices is \"24000\". The default value for long-form voices is \"24000\". The default value for generative voices is \"24000\".</p> <p>Valid values for pcm are \"8000\" and \"16000\" The default value is \"16000\". </p> <p>Valid value for ogg_opus is \"48000\". </p> <p>Valid value for mu-law and a-law is \"8000\". </p>"""
    sns_topic_arn: NotRequired["aws_sdk_polly.types.sns_topic_arn.SnsTopicArn"]
    """<p>ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.</p>"""
    speech_mark_types: NotRequired[
        "aws_sdk_polly.types.speech_mark_type_list.SpeechMarkTypeList"
    ]
    """<p>The type of speech marks returned for the input text.</p>"""
    text: "aws_sdk_polly.types.text.Text"
    """<p>The input text to synthesize. If you specify ssml as the TextType, follow the SSML format for the input text. </p>"""
    text_type: NotRequired["aws_sdk_polly.types.text_type.TextType"]
    """<p>Specifies whether the input text is plain text or SSML. The default value is plain text. </p>"""
    voice_id: "aws_sdk_polly.types.voice_id.VoiceId"
    """<p>Voice ID to use for the synthesis. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSpeechSynthesisTaskInput) -> dict:
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
    out["OutputS3BucketName"] = value["output_s3_bucket_name"]
    if "output_s3_key_prefix" in value:
        out["OutputS3KeyPrefix"] = value["output_s3_key_prefix"]
    if "sample_rate" in value:
        out["SampleRate"] = value["sample_rate"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
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


def deserialize_json(data: dict) -> StartSpeechSynthesisTaskInput:
    out: StartSpeechSynthesisTaskInput = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError(
            "StartSpeechSynthesisTaskInput.output_format required"
        )
    if "OutputS3BucketName" in data:
        out["output_s3_bucket_name"] = data["OutputS3BucketName"]
    else:
        raise DeserializationError(
            "StartSpeechSynthesisTaskInput.output_s3_bucket_name required"
        )
    if "OutputS3KeyPrefix" in data:
        out["output_s3_key_prefix"] = data["OutputS3KeyPrefix"]
    if "SampleRate" in data:
        out["sample_rate"] = data["SampleRate"]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
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
        raise DeserializationError("StartSpeechSynthesisTaskInput.text required")
    if "TextType" in data:
        import aws_sdk_polly.types.text_type

        out["text_type"] = aws_sdk_polly.types.text_type.deserialize_json(
            data["TextType"]
        )
    if "VoiceId" in data:
        import aws_sdk_polly.types.voice_id

        out["voice_id"] = aws_sdk_polly.types.voice_id.deserialize_json(data["VoiceId"])
    else:
        raise DeserializationError("StartSpeechSynthesisTaskInput.voice_id required")
    return out
