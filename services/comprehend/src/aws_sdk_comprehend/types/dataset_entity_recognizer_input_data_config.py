"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetEntityRecognizerInputDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.dataset_entity_recognizer_annotations
    import aws_sdk_comprehend.types.dataset_entity_recognizer_documents
    import aws_sdk_comprehend.types.dataset_entity_recognizer_entity_list


class DatasetEntityRecognizerInputDataConfig(TypedDict):
    annotations: NotRequired[
        "aws_sdk_comprehend.types.dataset_entity_recognizer_annotations.DatasetEntityRecognizerAnnotations"
    ]
    """<p>The S3 location of the annotation documents for your custom entity recognizer.</p>"""
    documents: "aws_sdk_comprehend.types.dataset_entity_recognizer_documents.DatasetEntityRecognizerDocuments"
    """<p>The format and location of the training documents for your custom entity recognizer.</p>"""
    entity_list: NotRequired[
        "aws_sdk_comprehend.types.dataset_entity_recognizer_entity_list.DatasetEntityRecognizerEntityList"
    ]
    """<p>The S3 location of the entity list for your custom entity recognizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetEntityRecognizerInputDataConfig) -> dict:
    out: dict = {}
    if "annotations" in value:
        import aws_sdk_comprehend.types.dataset_entity_recognizer_annotations

        out["Annotations"] = (
            aws_sdk_comprehend.types.dataset_entity_recognizer_annotations.serialize_aws_json_1_1(
                value["annotations"]
            )
        )
    import aws_sdk_comprehend.types.dataset_entity_recognizer_documents

    out["Documents"] = (
        aws_sdk_comprehend.types.dataset_entity_recognizer_documents.serialize_aws_json_1_1(
            value["documents"]
        )
    )
    if "entity_list" in value:
        import aws_sdk_comprehend.types.dataset_entity_recognizer_entity_list

        out["EntityList"] = (
            aws_sdk_comprehend.types.dataset_entity_recognizer_entity_list.serialize_aws_json_1_1(
                value["entity_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetEntityRecognizerInputDataConfig:
    out: DatasetEntityRecognizerInputDataConfig = {}  # type: ignore[typeddict-item]
    if "Annotations" in data:
        import aws_sdk_comprehend.types.dataset_entity_recognizer_annotations

        out["annotations"] = (
            aws_sdk_comprehend.types.dataset_entity_recognizer_annotations.deserialize_aws_json_1_1(
                data["Annotations"]
            )
        )
    if "Documents" in data:
        import aws_sdk_comprehend.types.dataset_entity_recognizer_documents

        out["documents"] = (
            aws_sdk_comprehend.types.dataset_entity_recognizer_documents.deserialize_aws_json_1_1(
                data["Documents"]
            )
        )
    else:
        raise DeserializationError(
            "DatasetEntityRecognizerInputDataConfig.documents required"
        )
    if "EntityList" in data:
        import aws_sdk_comprehend.types.dataset_entity_recognizer_entity_list

        out["entity_list"] = (
            aws_sdk_comprehend.types.dataset_entity_recognizer_entity_list.deserialize_aws_json_1_1(
                data["EntityList"]
            )
        )
    return out
