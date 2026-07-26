"""Generated from Smithy shape ``com.amazonaws.configservice#GetResourceEvaluationSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.compliance_type
    import capo_config_service.types.date
    import capo_config_service.types.evaluation_context
    import capo_config_service.types.evaluation_mode
    import capo_config_service.types.evaluation_status
    import capo_config_service.types.resource_details
    import capo_config_service.types.resource_evaluation_id


class GetResourceEvaluationSummaryResponse(TypedDict, closed=True):
    resource_evaluation_id: NotRequired[
        "capo_config_service.types.resource_evaluation_id.ResourceEvaluationId"
    ]
    """<p>The unique <code>ResourceEvaluationId</code> of Amazon Web Services resource execution for which you want to retrieve the evaluation summary.</p>"""
    evaluation_mode: NotRequired[
        "capo_config_service.types.evaluation_mode.EvaluationMode"
    ]
    """<p>Lists results of the mode that you requested to retrieve the resource evaluation summary. The valid values are Detective or Proactive.</p>"""
    evaluation_status: NotRequired[
        "capo_config_service.types.evaluation_status.EvaluationStatus"
    ]
    """<p>Returns an <code>EvaluationStatus</code> object.</p>"""
    evaluation_start_timestamp: NotRequired["capo_config_service.types.date.Date"]
    """<p>The start timestamp when Config rule starts evaluating compliance for the provided resource details.</p>"""
    compliance: NotRequired["capo_config_service.types.compliance_type.ComplianceType"]
    """<p>The compliance status of the resource evaluation summary.</p>"""
    evaluation_context: NotRequired[
        "capo_config_service.types.evaluation_context.EvaluationContext"
    ]
    """<p>Returns an <code>EvaluationContext</code> object.</p>"""
    resource_details: NotRequired[
        "capo_config_service.types.resource_details.ResourceDetails"
    ]
    """<p>Returns a <code>ResourceDetails</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceEvaluationSummaryResponse) -> dict:
    out: dict = {}
    if "resource_evaluation_id" in value:
        out["ResourceEvaluationId"] = value["resource_evaluation_id"]
    if "evaluation_mode" in value:
        import capo_config_service.types.evaluation_mode

        out["EvaluationMode"] = (
            capo_config_service.types.evaluation_mode.serialize_aws_json_1_1(
                value["evaluation_mode"]
            )
        )
    if "evaluation_status" in value:
        import capo_config_service.types.evaluation_status

        out["EvaluationStatus"] = (
            capo_config_service.types.evaluation_status.serialize_aws_json_1_1(
                value["evaluation_status"]
            )
        )
    if "evaluation_start_timestamp" in value:
        import capo_config_service.types.date

        out["EvaluationStartTimestamp"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["evaluation_start_timestamp"]
            )
        )
    if "compliance" in value:
        import capo_config_service.types.compliance_type

        out["Compliance"] = (
            capo_config_service.types.compliance_type.serialize_aws_json_1_1(
                value["compliance"]
            )
        )
    if "evaluation_context" in value:
        import capo_config_service.types.evaluation_context

        out["EvaluationContext"] = (
            capo_config_service.types.evaluation_context.serialize_aws_json_1_1(
                value["evaluation_context"]
            )
        )
    if "resource_details" in value:
        import capo_config_service.types.resource_details

        out["ResourceDetails"] = (
            capo_config_service.types.resource_details.serialize_aws_json_1_1(
                value["resource_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceEvaluationSummaryResponse:
    out: GetResourceEvaluationSummaryResponse = {}  # type: ignore[typeddict-item]
    if "ResourceEvaluationId" in data:
        out["resource_evaluation_id"] = data["ResourceEvaluationId"]
    if "EvaluationMode" in data:
        import capo_config_service.types.evaluation_mode

        out["evaluation_mode"] = (
            capo_config_service.types.evaluation_mode.deserialize_aws_json_1_1(
                data["EvaluationMode"]
            )
        )
    if "EvaluationStatus" in data:
        import capo_config_service.types.evaluation_status

        out["evaluation_status"] = (
            capo_config_service.types.evaluation_status.deserialize_aws_json_1_1(
                data["EvaluationStatus"]
            )
        )
    if "EvaluationStartTimestamp" in data:
        import capo_config_service.types.date

        out["evaluation_start_timestamp"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["EvaluationStartTimestamp"]
            )
        )
    if "Compliance" in data:
        import capo_config_service.types.compliance_type

        out["compliance"] = (
            capo_config_service.types.compliance_type.deserialize_aws_json_1_1(
                data["Compliance"]
            )
        )
    if "EvaluationContext" in data:
        import capo_config_service.types.evaluation_context

        out["evaluation_context"] = (
            capo_config_service.types.evaluation_context.deserialize_aws_json_1_1(
                data["EvaluationContext"]
            )
        )
    if "ResourceDetails" in data:
        import capo_config_service.types.resource_details

        out["resource_details"] = (
            capo_config_service.types.resource_details.deserialize_aws_json_1_1(
                data["ResourceDetails"]
            )
        )
    return out
