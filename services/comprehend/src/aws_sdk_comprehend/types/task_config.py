"""Generated from Smithy shape ``com.amazonaws.comprehend#TaskConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classification_config
    import aws_sdk_comprehend.types.entity_recognition_config
    import aws_sdk_comprehend.types.language_code


class TaskConfig(TypedDict):
    language_code: "aws_sdk_comprehend.types.language_code.LanguageCode"
    """<p>Language code for the language that the model supports.</p>"""
    document_classification_config: NotRequired[
        "aws_sdk_comprehend.types.document_classification_config.DocumentClassificationConfig"
    ]
    """<p>Configuration required for a document classification model.</p>"""
    entity_recognition_config: NotRequired[
        "aws_sdk_comprehend.types.entity_recognition_config.EntityRecognitionConfig"
    ]
    """<p>Configuration required for an entity recognition model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskConfig) -> dict:
    out: dict = {}
    import aws_sdk_comprehend.types.language_code

    out["LanguageCode"] = aws_sdk_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "document_classification_config" in value:
        import aws_sdk_comprehend.types.document_classification_config

        out["DocumentClassificationConfig"] = (
            aws_sdk_comprehend.types.document_classification_config.serialize_aws_json_1_1(
                value["document_classification_config"]
            )
        )
    if "entity_recognition_config" in value:
        import aws_sdk_comprehend.types.entity_recognition_config

        out["EntityRecognitionConfig"] = (
            aws_sdk_comprehend.types.entity_recognition_config.serialize_aws_json_1_1(
                value["entity_recognition_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskConfig:
    out: TaskConfig = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("TaskConfig.language_code required")
    if "DocumentClassificationConfig" in data:
        import aws_sdk_comprehend.types.document_classification_config

        out["document_classification_config"] = (
            aws_sdk_comprehend.types.document_classification_config.deserialize_aws_json_1_1(
                data["DocumentClassificationConfig"]
            )
        )
    if "EntityRecognitionConfig" in data:
        import aws_sdk_comprehend.types.entity_recognition_config

        out["entity_recognition_config"] = (
            aws_sdk_comprehend.types.entity_recognition_config.deserialize_aws_json_1_1(
                data["EntityRecognitionConfig"]
            )
        )
    return out
