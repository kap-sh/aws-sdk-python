"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GetPlanEvaluationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_arc_region_switch.types.evaluation_status
    import aws_sdk_arc_region_switch.types.next_token
    import aws_sdk_arc_region_switch.types.plan_arn
    import aws_sdk_arc_region_switch.types.plan_warnings
    import aws_sdk_arc_region_switch.types.region


class GetPlanEvaluationStatusResponse(TypedDict, closed=True):
    plan_arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    last_evaluation_time: NotRequired["datetime.datetime"]
    """<p>The time of the last time that Region switch ran an evaluation of the plan.</p>"""
    last_evaluated_version: NotRequired["str"]
    """<p>The version of the last evaluation of the plan.</p>"""
    region: NotRequired["aws_sdk_arc_region_switch.types.region.Region"]
    """<p>The Amazon Web Services Region for the plan.</p>"""
    evaluation_state: NotRequired[
        "aws_sdk_arc_region_switch.types.evaluation_status.EvaluationStatus"
    ]
    """<p>The evaluation state for the plan.</p>"""
    warnings: NotRequired["aws_sdk_arc_region_switch.types.plan_warnings.PlanWarnings"]
    """<p>The current evaluation warnings for the plan. </p>"""
    next_token: NotRequired["aws_sdk_arc_region_switch.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPlanEvaluationStatusResponse) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    if "last_evaluation_time" in value:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["lastEvaluationTime"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_evaluation_time"]
            )
        )
    if "last_evaluated_version" in value:
        out["lastEvaluatedVersion"] = value["last_evaluated_version"]
    if "region" in value:
        out["region"] = value["region"]
    if "evaluation_state" in value:
        import aws_sdk_arc_region_switch.types.evaluation_status

        out["evaluationState"] = (
            aws_sdk_arc_region_switch.types.evaluation_status.serialize_aws_json_1_0(
                value["evaluation_state"]
            )
        )
    if "warnings" in value:
        import aws_sdk_arc_region_switch.types.plan_warnings

        out["warnings"] = (
            aws_sdk_arc_region_switch.types.plan_warnings.serialize_aws_json_1_0(
                value["warnings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPlanEvaluationStatusResponse:
    out: GetPlanEvaluationStatusResponse = {}  # type: ignore[typeddict-item]
    if "planArn" in data:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("GetPlanEvaluationStatusResponse.plan_arn required")
    if "lastEvaluationTime" in data:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["last_evaluation_time"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastEvaluationTime"]
            )
        )
    if "lastEvaluatedVersion" in data:
        out["last_evaluated_version"] = data["lastEvaluatedVersion"]
    if "region" in data:
        out["region"] = data["region"]
    if "evaluationState" in data:
        import aws_sdk_arc_region_switch.types.evaluation_status

        out["evaluation_state"] = (
            aws_sdk_arc_region_switch.types.evaluation_status.deserialize_aws_json_1_0(
                data["evaluationState"]
            )
        )
    if "warnings" in data:
        import aws_sdk_arc_region_switch.types.plan_warnings

        out["warnings"] = (
            aws_sdk_arc_region_switch.types.plan_warnings.deserialize_aws_json_1_0(
                data["warnings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
