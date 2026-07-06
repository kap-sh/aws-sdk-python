"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceEvaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.evaluation_mode
    import aws_sdk_config_service.types.resource_evaluation_id


class ResourceEvaluation(TypedDict, closed=True):
    resource_evaluation_id: NotRequired[
        "aws_sdk_config_service.types.resource_evaluation_id.ResourceEvaluationId"
    ]
    """<p>The ResourceEvaluationId of a evaluation.</p>"""
    evaluation_mode: NotRequired[
        "aws_sdk_config_service.types.evaluation_mode.EvaluationMode"
    ]
    """<p>The mode of an evaluation. The valid values are Detective or Proactive.</p>"""
    evaluation_start_timestamp: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The starting time of an execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceEvaluation) -> dict:
    out: dict = {}
    if "resource_evaluation_id" in value:
        out["ResourceEvaluationId"] = value["resource_evaluation_id"]
    if "evaluation_mode" in value:
        import aws_sdk_config_service.types.evaluation_mode

        out["EvaluationMode"] = (
            aws_sdk_config_service.types.evaluation_mode.serialize_aws_json_1_1(
                value["evaluation_mode"]
            )
        )
    if "evaluation_start_timestamp" in value:
        import aws_sdk_config_service.types.date

        out["EvaluationStartTimestamp"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["evaluation_start_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceEvaluation:
    out: ResourceEvaluation = {}  # type: ignore[typeddict-item]
    if "ResourceEvaluationId" in data:
        out["resource_evaluation_id"] = data["ResourceEvaluationId"]
    if "EvaluationMode" in data:
        import aws_sdk_config_service.types.evaluation_mode

        out["evaluation_mode"] = (
            aws_sdk_config_service.types.evaluation_mode.deserialize_aws_json_1_1(
                data["EvaluationMode"]
            )
        )
    if "EvaluationStartTimestamp" in data:
        import aws_sdk_config_service.types.date

        out["evaluation_start_timestamp"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["EvaluationStartTimestamp"]
            )
        )
    return out
