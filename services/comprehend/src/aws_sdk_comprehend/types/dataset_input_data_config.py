"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetInputDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.dataset_augmented_manifests_list
    import aws_sdk_comprehend.types.dataset_data_format
    import aws_sdk_comprehend.types.dataset_document_classifier_input_data_config
    import aws_sdk_comprehend.types.dataset_entity_recognizer_input_data_config


class DatasetInputDataConfig(TypedDict):
    augmented_manifests: NotRequired[
        "aws_sdk_comprehend.types.dataset_augmented_manifests_list.DatasetAugmentedManifestsList"
    ]
    """<p>A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth. </p>"""
    data_format: NotRequired[
        "aws_sdk_comprehend.types.dataset_data_format.DatasetDataFormat"
    ]
    """<p> <code>COMPREHEND_CSV</code>: The data format is a two-column CSV file, where the first column contains labels and the second column contains documents.</p> <p> <code>AUGMENTED_MANIFEST</code>: The data format </p>"""
    document_classifier_input_data_config: NotRequired[
        "aws_sdk_comprehend.types.dataset_document_classifier_input_data_config.DatasetDocumentClassifierInputDataConfig"
    ]
    r"""<p>The input properties for training a document classifier model. </p> <p>For more information on how the input file is formatted, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data.html\">Preparing training data</a> in the Comprehend Developer Guide. </p>"""
    entity_recognizer_input_data_config: NotRequired[
        "aws_sdk_comprehend.types.dataset_entity_recognizer_input_data_config.DatasetEntityRecognizerInputDataConfig"
    ]
    """<p>The input properties for training an entity recognizer model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetInputDataConfig) -> dict:
    out: dict = {}
    if "augmented_manifests" in value:
        import aws_sdk_comprehend.types.dataset_augmented_manifests_list

        out["AugmentedManifests"] = (
            aws_sdk_comprehend.types.dataset_augmented_manifests_list.serialize_aws_json_1_1(
                value["augmented_manifests"]
            )
        )
    if "data_format" in value:
        import aws_sdk_comprehend.types.dataset_data_format

        out["DataFormat"] = (
            aws_sdk_comprehend.types.dataset_data_format.serialize_aws_json_1_1(
                value["data_format"]
            )
        )
    if "document_classifier_input_data_config" in value:
        import aws_sdk_comprehend.types.dataset_document_classifier_input_data_config

        out["DocumentClassifierInputDataConfig"] = (
            aws_sdk_comprehend.types.dataset_document_classifier_input_data_config.serialize_aws_json_1_1(
                value["document_classifier_input_data_config"]
            )
        )
    if "entity_recognizer_input_data_config" in value:
        import aws_sdk_comprehend.types.dataset_entity_recognizer_input_data_config

        out["EntityRecognizerInputDataConfig"] = (
            aws_sdk_comprehend.types.dataset_entity_recognizer_input_data_config.serialize_aws_json_1_1(
                value["entity_recognizer_input_data_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetInputDataConfig:
    out: DatasetInputDataConfig = {}  # type: ignore[typeddict-item]
    if "AugmentedManifests" in data:
        import aws_sdk_comprehend.types.dataset_augmented_manifests_list

        out["augmented_manifests"] = (
            aws_sdk_comprehend.types.dataset_augmented_manifests_list.deserialize_aws_json_1_1(
                data["AugmentedManifests"]
            )
        )
    if "DataFormat" in data:
        import aws_sdk_comprehend.types.dataset_data_format

        out["data_format"] = (
            aws_sdk_comprehend.types.dataset_data_format.deserialize_aws_json_1_1(
                data["DataFormat"]
            )
        )
    if "DocumentClassifierInputDataConfig" in data:
        import aws_sdk_comprehend.types.dataset_document_classifier_input_data_config

        out["document_classifier_input_data_config"] = (
            aws_sdk_comprehend.types.dataset_document_classifier_input_data_config.deserialize_aws_json_1_1(
                data["DocumentClassifierInputDataConfig"]
            )
        )
    if "EntityRecognizerInputDataConfig" in data:
        import aws_sdk_comprehend.types.dataset_entity_recognizer_input_data_config

        out["entity_recognizer_input_data_config"] = (
            aws_sdk_comprehend.types.dataset_entity_recognizer_input_data_config.deserialize_aws_json_1_1(
                data["EntityRecognizerInputDataConfig"]
            )
        )
    return out
