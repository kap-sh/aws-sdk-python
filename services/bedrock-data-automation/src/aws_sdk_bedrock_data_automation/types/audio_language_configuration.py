"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioLanguageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.audio_generative_output_language
    import aws_sdk_bedrock_data_automation.types.audio_input_languages


class AudioLanguageConfiguration(TypedDict, closed=True):
    input_languages: NotRequired[
        "aws_sdk_bedrock_data_automation.types.audio_input_languages.AudioInputLanguages"
    ]
    generative_output_language: NotRequired[
        "aws_sdk_bedrock_data_automation.types.audio_generative_output_language.AudioGenerativeOutputLanguage"
    ]
    identify_multiple_languages: NotRequired["bool"]
    """Enable multiple language identification in audio"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioLanguageConfiguration) -> dict:
    out: dict = {}
    if "input_languages" in value:
        import aws_sdk_bedrock_data_automation.types.audio_input_languages

        out["inputLanguages"] = (
            aws_sdk_bedrock_data_automation.types.audio_input_languages.serialize_json(
                value["input_languages"]
            )
        )
    if "generative_output_language" in value:
        import aws_sdk_bedrock_data_automation.types.audio_generative_output_language

        out["generativeOutputLanguage"] = (
            aws_sdk_bedrock_data_automation.types.audio_generative_output_language.serialize_json(
                value["generative_output_language"]
            )
        )
    if "identify_multiple_languages" in value:
        out["identifyMultipleLanguages"] = value["identify_multiple_languages"]
    return out


def deserialize_json(data: dict) -> AudioLanguageConfiguration:
    out: AudioLanguageConfiguration = {}  # type: ignore[typeddict-item]
    if "inputLanguages" in data:
        import aws_sdk_bedrock_data_automation.types.audio_input_languages

        out["input_languages"] = (
            aws_sdk_bedrock_data_automation.types.audio_input_languages.deserialize_json(
                data["inputLanguages"]
            )
        )
    if "generativeOutputLanguage" in data:
        import aws_sdk_bedrock_data_automation.types.audio_generative_output_language

        out["generative_output_language"] = (
            aws_sdk_bedrock_data_automation.types.audio_generative_output_language.deserialize_json(
                data["generativeOutputLanguage"]
            )
        )
    if "identifyMultipleLanguages" in data:
        out["identify_multiple_languages"] = data["identifyMultipleLanguages"]
    return out
