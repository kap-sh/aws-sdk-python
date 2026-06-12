"""Generated from Smithy shape ``com.amazonaws.translate#TranslateDocumentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.applied_terminology_list
    import aws_sdk_translate.types.language_code_string
    import aws_sdk_translate.types.translated_document
    import aws_sdk_translate.types.translation_settings


class TranslateDocumentResponse(TypedDict):
    translated_document: (
        "aws_sdk_translate.types.translated_document.TranslatedDocument"
    )
    """<p>The document containing the translated content. The document format matches the source document format.</p>"""
    source_language_code: (
        "aws_sdk_translate.types.language_code_string.LanguageCodeString"
    )
    """<p>The language code of the source document.</p>"""
    target_language_code: (
        "aws_sdk_translate.types.language_code_string.LanguageCodeString"
    )
    """<p>The language code of the translated document. </p>"""
    applied_terminologies: NotRequired[
        "aws_sdk_translate.types.applied_terminology_list.AppliedTerminologyList"
    ]
    """<p>The names of the custom terminologies applied to the input text by Amazon Translate to produce the translated text document.</p>"""
    applied_settings: NotRequired[
        "aws_sdk_translate.types.translation_settings.TranslationSettings"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranslateDocumentResponse) -> dict:
    out: dict = {}
    import aws_sdk_translate.types.translated_document

    out["TranslatedDocument"] = (
        aws_sdk_translate.types.translated_document.serialize_aws_json_1_1(
            value["translated_document"]
        )
    )
    out["SourceLanguageCode"] = value["source_language_code"]
    out["TargetLanguageCode"] = value["target_language_code"]
    if "applied_terminologies" in value:
        import aws_sdk_translate.types.applied_terminology_list

        out["AppliedTerminologies"] = (
            aws_sdk_translate.types.applied_terminology_list.serialize_aws_json_1_1(
                value["applied_terminologies"]
            )
        )
    if "applied_settings" in value:
        import aws_sdk_translate.types.translation_settings

        out["AppliedSettings"] = (
            aws_sdk_translate.types.translation_settings.serialize_aws_json_1_1(
                value["applied_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TranslateDocumentResponse:
    out: TranslateDocumentResponse = {}  # type: ignore[typeddict-item]
    if "TranslatedDocument" in data:
        import aws_sdk_translate.types.translated_document

        out["translated_document"] = (
            aws_sdk_translate.types.translated_document.deserialize_aws_json_1_1(
                data["TranslatedDocument"]
            )
        )
    else:
        raise DeserializationError(
            "TranslateDocumentResponse.translated_document required"
        )
    if "SourceLanguageCode" in data:
        out["source_language_code"] = data["SourceLanguageCode"]
    else:
        raise DeserializationError(
            "TranslateDocumentResponse.source_language_code required"
        )
    if "TargetLanguageCode" in data:
        out["target_language_code"] = data["TargetLanguageCode"]
    else:
        raise DeserializationError(
            "TranslateDocumentResponse.target_language_code required"
        )
    if "AppliedTerminologies" in data:
        import aws_sdk_translate.types.applied_terminology_list

        out["applied_terminologies"] = (
            aws_sdk_translate.types.applied_terminology_list.deserialize_aws_json_1_1(
                data["AppliedTerminologies"]
            )
        )
    if "AppliedSettings" in data:
        import aws_sdk_translate.types.translation_settings

        out["applied_settings"] = (
            aws_sdk_translate.types.translation_settings.deserialize_aws_json_1_1(
                data["AppliedSettings"]
            )
        )
    return out
