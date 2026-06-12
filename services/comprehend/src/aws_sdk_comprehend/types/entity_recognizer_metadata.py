"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_recognizer_evaluation_metrics
    import aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list
    import aws_sdk_comprehend.types.integer


class EntityRecognizerMetadata(TypedDict):
    number_of_trained_documents: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p> The number of documents in the input data that were used to train the entity recognizer. Typically this is 80 to 90 percent of the input documents.</p>"""
    number_of_test_documents: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p> The number of documents in the input data that were used to test the entity recognizer. Typically this is 10 to 20 percent of the input documents.</p>"""
    evaluation_metrics: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_evaluation_metrics.EntityRecognizerEvaluationMetrics"
    ]
    """<p>Detailed information about the accuracy of an entity recognizer.</p>"""
    entity_types: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list.EntityRecognizerMetadataEntityTypesList"
    ]
    """<p>Entity types from the metadata of an entity recognizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerMetadata) -> dict:
    out: dict = {}
    if "number_of_trained_documents" in value:
        out["NumberOfTrainedDocuments"] = value["number_of_trained_documents"]
    if "number_of_test_documents" in value:
        out["NumberOfTestDocuments"] = value["number_of_test_documents"]
    if "evaluation_metrics" in value:
        import aws_sdk_comprehend.types.entity_recognizer_evaluation_metrics

        out["EvaluationMetrics"] = (
            aws_sdk_comprehend.types.entity_recognizer_evaluation_metrics.serialize_aws_json_1_1(
                value["evaluation_metrics"]
            )
        )
    if "entity_types" in value:
        import aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list

        out["EntityTypes"] = (
            aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list.serialize_aws_json_1_1(
                value["entity_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerMetadata:
    out: EntityRecognizerMetadata = {}  # type: ignore[typeddict-item]
    if "NumberOfTrainedDocuments" in data:
        out["number_of_trained_documents"] = data["NumberOfTrainedDocuments"]
    if "NumberOfTestDocuments" in data:
        out["number_of_test_documents"] = data["NumberOfTestDocuments"]
    if "EvaluationMetrics" in data:
        import aws_sdk_comprehend.types.entity_recognizer_evaluation_metrics

        out["evaluation_metrics"] = (
            aws_sdk_comprehend.types.entity_recognizer_evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluationMetrics"]
            )
        )
    if "EntityTypes" in data:
        import aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list

        out["entity_types"] = (
            aws_sdk_comprehend.types.entity_recognizer_metadata_entity_types_list.deserialize_aws_json_1_1(
                data["EntityTypes"]
            )
        )
    return out
