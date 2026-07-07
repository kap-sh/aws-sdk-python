"""Generated from Smithy shape ``com.amazonaws.configservice#GetResourceEvaluationSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.compliance_type
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.evaluation_context
    import aws_sdk_config_service.types.evaluation_mode
    import aws_sdk_config_service.types.evaluation_status
    import aws_sdk_config_service.types.resource_details
    import aws_sdk_config_service.types.resource_evaluation_id


class GetResourceEvaluationSummaryResponse(TypedDict, closed=True):
    resource_evaluation_id: NotRequired[
        "aws_sdk_config_service.types.resource_evaluation_id.ResourceEvaluationId"
    ]
    """<p>The unique <code>ResourceEvaluationId</code> of Amazon Web Services resource execution for which you want to retrieve the evaluation summary.</p>"""
    evaluation_mode: NotRequired[
        "aws_sdk_config_service.types.evaluation_mode.EvaluationMode"
    ]
    """<p>Lists results of the mode that you requested to retrieve the resource evaluation summary. The valid values are Detective or Proactive.</p>"""
    evaluation_status: NotRequired[
        "aws_sdk_config_service.types.evaluation_status.EvaluationStatus"
    ]
    """<p>Returns an <code>EvaluationStatus</code> object.</p>"""
    evaluation_start_timestamp: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The start timestamp when Config rule starts evaluating compliance for the provided resource details.</p>"""
    compliance: NotRequired[
        "aws_sdk_config_service.types.compliance_type.ComplianceType"
    ]
    """<p>The compliance status of the resource evaluation summary.</p>"""
    evaluation_context: NotRequired[
        "aws_sdk_config_service.types.evaluation_context.EvaluationContext"
    ]
    """<p>Returns an <code>EvaluationContext</code> object.</p>"""
    resource_details: NotRequired[
        "aws_sdk_config_service.types.resource_details.ResourceDetails"
    ]
    """<p>Returns a <code>ResourceDetails</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceEvaluationSummaryResponse) -> dict:
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
    if "evaluation_status" in value:
        import aws_sdk_config_service.types.evaluation_status

        out["EvaluationStatus"] = (
            aws_sdk_config_service.types.evaluation_status.serialize_aws_json_1_1(
                value["evaluation_status"]
            )
        )
    if "evaluation_start_timestamp" in value:
        import aws_sdk_config_service.types.date

        out["EvaluationStartTimestamp"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["evaluation_start_timestamp"]
            )
        )
    if "compliance" in value:
        import aws_sdk_config_service.types.compliance_type

        out["Compliance"] = (
            aws_sdk_config_service.types.compliance_type.serialize_aws_json_1_1(
                value["compliance"]
            )
        )
    if "evaluation_context" in value:
        import aws_sdk_config_service.types.evaluation_context

        out["EvaluationContext"] = (
            aws_sdk_config_service.types.evaluation_context.serialize_aws_json_1_1(
                value["evaluation_context"]
            )
        )
    if "resource_details" in value:
        import aws_sdk_config_service.types.resource_details

        out["ResourceDetails"] = (
            aws_sdk_config_service.types.resource_details.serialize_aws_json_1_1(
                value["resource_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceEvaluationSummaryResponse:
    out: GetResourceEvaluationSummaryResponse = {}  # type: ignore[typeddict-item]
    if "ResourceEvaluationId" in data:
        out["resource_evaluation_id"] = data["ResourceEvaluationId"]
    if "EvaluationMode" in data:
        import aws_sdk_config_service.types.evaluation_mode

        out["evaluation_mode"] = (
            aws_sdk_config_service.types.evaluation_mode.deserialize_aws_json_1_1(
                data["EvaluationMode"]
            )
        )
    if "EvaluationStatus" in data:
        import aws_sdk_config_service.types.evaluation_status

        out["evaluation_status"] = (
            aws_sdk_config_service.types.evaluation_status.deserialize_aws_json_1_1(
                data["EvaluationStatus"]
            )
        )
    if "EvaluationStartTimestamp" in data:
        import aws_sdk_config_service.types.date

        out["evaluation_start_timestamp"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["EvaluationStartTimestamp"]
            )
        )
    if "Compliance" in data:
        import aws_sdk_config_service.types.compliance_type

        out["compliance"] = (
            aws_sdk_config_service.types.compliance_type.deserialize_aws_json_1_1(
                data["Compliance"]
            )
        )
    if "EvaluationContext" in data:
        import aws_sdk_config_service.types.evaluation_context

        out["evaluation_context"] = (
            aws_sdk_config_service.types.evaluation_context.deserialize_aws_json_1_1(
                data["EvaluationContext"]
            )
        )
    if "ResourceDetails" in data:
        import aws_sdk_config_service.types.resource_details

        out["resource_details"] = (
            aws_sdk_config_service.types.resource_details.deserialize_aws_json_1_1(
                data["ResourceDetails"]
            )
        )
    return out
