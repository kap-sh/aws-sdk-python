"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationResultIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.date
    import capo_config_service.types.evaluation_result_qualifier
    import capo_config_service.types.resource_evaluation_id


class EvaluationResultIdentifier(TypedDict, closed=True):
    evaluation_result_qualifier: NotRequired[
        "capo_config_service.types.evaluation_result_qualifier.EvaluationResultQualifier"
    ]
    """<p>Identifies an Config rule used to evaluate an Amazon Web Services resource, and provides the type and ID of the evaluated resource.</p>"""
    ordering_timestamp: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time of the event that triggered the evaluation of your Amazon Web Services resources. The time can indicate when Config delivered a configuration item change notification, or it can indicate when Config delivered the configuration snapshot, depending on which event triggered the evaluation.</p>"""
    resource_evaluation_id: NotRequired[
        "capo_config_service.types.resource_evaluation_id.ResourceEvaluationId"
    ]
    """<p>A Unique ID for an evaluation result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationResultIdentifier) -> dict:
    out: dict = {}
    if "evaluation_result_qualifier" in value:
        import capo_config_service.types.evaluation_result_qualifier

        out["EvaluationResultQualifier"] = (
            capo_config_service.types.evaluation_result_qualifier.serialize_aws_json_1_1(
                value["evaluation_result_qualifier"]
            )
        )
    if "ordering_timestamp" in value:
        import capo_config_service.types.date

        out["OrderingTimestamp"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["ordering_timestamp"]
            )
        )
    if "resource_evaluation_id" in value:
        out["ResourceEvaluationId"] = value["resource_evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationResultIdentifier:
    out: EvaluationResultIdentifier = {}  # type: ignore[typeddict-item]
    if "EvaluationResultQualifier" in data:
        import capo_config_service.types.evaluation_result_qualifier

        out["evaluation_result_qualifier"] = (
            capo_config_service.types.evaluation_result_qualifier.deserialize_aws_json_1_1(
                data["EvaluationResultQualifier"]
            )
        )
    if "OrderingTimestamp" in data:
        import capo_config_service.types.date

        out["ordering_timestamp"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["OrderingTimestamp"]
            )
        )
    if "ResourceEvaluationId" in data:
        out["resource_evaluation_id"] = data["ResourceEvaluationId"]
    return out
