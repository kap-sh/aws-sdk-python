"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerMetadataEntityTypesListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.any_length_string
    import aws_sdk_comprehend.types.entity_types_evaluation_metrics
    import aws_sdk_comprehend.types.integer


class EntityRecognizerMetadataEntityTypesListItem(TypedDict, closed=True):
    type: NotRequired["aws_sdk_comprehend.types.any_length_string.AnyLengthString"]
    """<p>Type of entity from the list of entity types in the metadata of an entity recognizer. </p>"""
    evaluation_metrics: NotRequired[
        "aws_sdk_comprehend.types.entity_types_evaluation_metrics.EntityTypesEvaluationMetrics"
    ]
    """<p>Detailed information about the accuracy of the entity recognizer for a specific item on the list of entity types. </p>"""
    number_of_train_mentions: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Indicates the number of times the given entity type was seen in the training data. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerMetadataEntityTypesListItem) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "evaluation_metrics" in value:
        import aws_sdk_comprehend.types.entity_types_evaluation_metrics

        out["EvaluationMetrics"] = (
            aws_sdk_comprehend.types.entity_types_evaluation_metrics.serialize_aws_json_1_1(
                value["evaluation_metrics"]
            )
        )
    if "number_of_train_mentions" in value:
        out["NumberOfTrainMentions"] = value["number_of_train_mentions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerMetadataEntityTypesListItem:
    out: EntityRecognizerMetadataEntityTypesListItem = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "EvaluationMetrics" in data:
        import aws_sdk_comprehend.types.entity_types_evaluation_metrics

        out["evaluation_metrics"] = (
            aws_sdk_comprehend.types.entity_types_evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluationMetrics"]
            )
        )
    if "NumberOfTrainMentions" in data:
        out["number_of_train_mentions"] = data["NumberOfTrainMentions"]
    return out
