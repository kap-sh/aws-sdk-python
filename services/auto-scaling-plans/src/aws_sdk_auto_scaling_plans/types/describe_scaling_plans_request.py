"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#DescribeScalingPlansRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.application_sources
    import aws_sdk_auto_scaling_plans.types.max_results
    import aws_sdk_auto_scaling_plans.types.next_token
    import aws_sdk_auto_scaling_plans.types.scaling_plan_names
    import aws_sdk_auto_scaling_plans.types.scaling_plan_version


class DescribeScalingPlansRequest(TypedDict):
    scaling_plan_names: NotRequired[
        "aws_sdk_auto_scaling_plans.types.scaling_plan_names.ScalingPlanNames"
    ]
    """<p>The names of the scaling plans (up to 10). If you specify application sources, you cannot specify scaling plan names.</p>"""
    scaling_plan_version: NotRequired[
        "aws_sdk_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    ]
    """<p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p> <note> <p>If you specify a scaling plan version, you must also specify a scaling plan name.</p> </note>"""
    application_sources: NotRequired[
        "aws_sdk_auto_scaling_plans.types.application_sources.ApplicationSources"
    ]
    """<p>The sources for the applications (up to 10). If you specify scaling plan names, you cannot specify application sources.</p>"""
    max_results: NotRequired["aws_sdk_auto_scaling_plans.types.max_results.MaxResults"]
    """<p>The maximum number of scalable resources to return. This value can be between 1 and 50. The default value is 50.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling_plans.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalingPlansRequest) -> dict:
    out: dict = {}
    if "scaling_plan_names" in value:
        import aws_sdk_auto_scaling_plans.types.scaling_plan_names

        out["ScalingPlanNames"] = (
            aws_sdk_auto_scaling_plans.types.scaling_plan_names.serialize_aws_json_1_1(
                value["scaling_plan_names"]
            )
        )
    if "scaling_plan_version" in value:
        out["ScalingPlanVersion"] = value["scaling_plan_version"]
    if "application_sources" in value:
        import aws_sdk_auto_scaling_plans.types.application_sources

        out["ApplicationSources"] = (
            aws_sdk_auto_scaling_plans.types.application_sources.serialize_aws_json_1_1(
                value["application_sources"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalingPlansRequest:
    out: DescribeScalingPlansRequest = {}  # type: ignore[typeddict-item]
    if "ScalingPlanNames" in data:
        import aws_sdk_auto_scaling_plans.types.scaling_plan_names

        out["scaling_plan_names"] = (
            aws_sdk_auto_scaling_plans.types.scaling_plan_names.deserialize_aws_json_1_1(
                data["ScalingPlanNames"]
            )
        )
    if "ScalingPlanVersion" in data:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    if "ApplicationSources" in data:
        import aws_sdk_auto_scaling_plans.types.application_sources

        out["application_sources"] = (
            aws_sdk_auto_scaling_plans.types.application_sources.deserialize_aws_json_1_1(
                data["ApplicationSources"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
