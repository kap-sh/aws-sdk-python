"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerInputDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_recognizer_annotations
    import aws_sdk_comprehend.types.entity_recognizer_augmented_manifests_list
    import aws_sdk_comprehend.types.entity_recognizer_data_format
    import aws_sdk_comprehend.types.entity_recognizer_documents
    import aws_sdk_comprehend.types.entity_recognizer_entity_list
    import aws_sdk_comprehend.types.entity_types_list


class EntityRecognizerInputDataConfig(TypedDict):
    data_format: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_data_format.EntityRecognizerDataFormat"
    ]
    """<p>The format of your training data:</p> <ul> <li> <p> <code>COMPREHEND_CSV</code>: A CSV file that supplements your training documents. The CSV file contains information about the custom entities that your trained model will detect. The required format of the file depends on whether you are providing annotations or an entity list.</p> <p>If you use this value, you must provide your CSV file by using either the <code>Annotations</code> or <code>EntityList</code> parameters. You must provide your training documents by using the <code>Documents</code> parameter.</p> </li> <li> <p> <code>AUGMENTED_MANIFEST</code>: A labeled dataset that is produced by Amazon SageMaker Ground Truth. This file is in JSON lines format. Each line is a complete JSON object that contains a training document and its labels. Each label annotates a named entity in the training document. </p> <p>If you use this value, you must provide the <code>AugmentedManifests</code> parameter in your request.</p> </li> </ul> <p>If you don't specify a value, Amazon Comprehend uses <code>COMPREHEND_CSV</code> as the default.</p>"""
    entity_types: "aws_sdk_comprehend.types.entity_types_list.EntityTypesList"
    """<p>The entity types in the labeled training data that Amazon Comprehend uses to train the custom entity recognizer. Any entity types that you don't specify are ignored.</p> <p>A maximum of 25 entity types can be used at one time to train an entity recognizer. Entity types must not contain the following invalid characters: \n (line break), \\n (escaped line break), \r (carriage return), \\r (escaped carriage return), \t (tab), \\t (escaped tab), space, and , (comma). </p>"""
    documents: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_documents.EntityRecognizerDocuments"
    ]
    """<p>The S3 location of the folder that contains the training documents for your custom entity recognizer.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>COMPREHEND_CSV</code>.</p>"""
    annotations: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_annotations.EntityRecognizerAnnotations"
    ]
    """<p>The S3 location of the CSV file that annotates your training documents.</p>"""
    entity_list: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_entity_list.EntityRecognizerEntityList"
    ]
    """<p>The S3 location of the CSV file that has the entity list for your custom entity recognizer.</p>"""
    augmented_manifests: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_augmented_manifests_list.EntityRecognizerAugmentedManifestsList"
    ]
    """<p>A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>AUGMENTED_MANIFEST</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerInputDataConfig) -> dict:
    out: dict = {}
    if "data_format" in value:
        import aws_sdk_comprehend.types.entity_recognizer_data_format

        out["DataFormat"] = (
            aws_sdk_comprehend.types.entity_recognizer_data_format.serialize_aws_json_1_1(
                value["data_format"]
            )
        )
    import aws_sdk_comprehend.types.entity_types_list

    out["EntityTypes"] = (
        aws_sdk_comprehend.types.entity_types_list.serialize_aws_json_1_1(
            value["entity_types"]
        )
    )
    if "documents" in value:
        import aws_sdk_comprehend.types.entity_recognizer_documents

        out["Documents"] = (
            aws_sdk_comprehend.types.entity_recognizer_documents.serialize_aws_json_1_1(
                value["documents"]
            )
        )
    if "annotations" in value:
        import aws_sdk_comprehend.types.entity_recognizer_annotations

        out["Annotations"] = (
            aws_sdk_comprehend.types.entity_recognizer_annotations.serialize_aws_json_1_1(
                value["annotations"]
            )
        )
    if "entity_list" in value:
        import aws_sdk_comprehend.types.entity_recognizer_entity_list

        out["EntityList"] = (
            aws_sdk_comprehend.types.entity_recognizer_entity_list.serialize_aws_json_1_1(
                value["entity_list"]
            )
        )
    if "augmented_manifests" in value:
        import aws_sdk_comprehend.types.entity_recognizer_augmented_manifests_list

        out["AugmentedManifests"] = (
            aws_sdk_comprehend.types.entity_recognizer_augmented_manifests_list.serialize_aws_json_1_1(
                value["augmented_manifests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerInputDataConfig:
    out: EntityRecognizerInputDataConfig = {}  # type: ignore[typeddict-item]
    if "DataFormat" in data:
        import aws_sdk_comprehend.types.entity_recognizer_data_format

        out["data_format"] = (
            aws_sdk_comprehend.types.entity_recognizer_data_format.deserialize_aws_json_1_1(
                data["DataFormat"]
            )
        )
    if "EntityTypes" in data:
        import aws_sdk_comprehend.types.entity_types_list

        out["entity_types"] = (
            aws_sdk_comprehend.types.entity_types_list.deserialize_aws_json_1_1(
                data["EntityTypes"]
            )
        )
    else:
        raise DeserializationError(
            "EntityRecognizerInputDataConfig.entity_types required"
        )
    if "Documents" in data:
        import aws_sdk_comprehend.types.entity_recognizer_documents

        out["documents"] = (
            aws_sdk_comprehend.types.entity_recognizer_documents.deserialize_aws_json_1_1(
                data["Documents"]
            )
        )
    if "Annotations" in data:
        import aws_sdk_comprehend.types.entity_recognizer_annotations

        out["annotations"] = (
            aws_sdk_comprehend.types.entity_recognizer_annotations.deserialize_aws_json_1_1(
                data["Annotations"]
            )
        )
    if "EntityList" in data:
        import aws_sdk_comprehend.types.entity_recognizer_entity_list

        out["entity_list"] = (
            aws_sdk_comprehend.types.entity_recognizer_entity_list.deserialize_aws_json_1_1(
                data["EntityList"]
            )
        )
    if "AugmentedManifests" in data:
        import aws_sdk_comprehend.types.entity_recognizer_augmented_manifests_list

        out["augmented_manifests"] = (
            aws_sdk_comprehend.types.entity_recognizer_augmented_manifests_list.deserialize_aws_json_1_1(
                data["AugmentedManifests"]
            )
        )
    return out
