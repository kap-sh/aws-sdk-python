"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#DescribeScalingPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.scaling_policies
    import capo_application_auto_scaling.types.xml_string


class DescribeScalingPoliciesResponse(TypedDict, closed=True):
    scaling_policies: NotRequired[
        "capo_application_auto_scaling.types.scaling_policies.ScalingPolicies"
    ]
    """<p>Information about the scaling policies.</p>"""
    next_token: NotRequired["capo_application_auto_scaling.types.xml_string.XmlString"]
    """<p>The token required to get the next set of results. This value is <code>null</code> if there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalingPoliciesResponse) -> dict:
    out: dict = {}
    if "scaling_policies" in value:
        import capo_application_auto_scaling.types.scaling_policies

        out["ScalingPolicies"] = (
            capo_application_auto_scaling.types.scaling_policies.serialize_aws_json_1_1(
                value["scaling_policies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalingPoliciesResponse:
    out: DescribeScalingPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "ScalingPolicies" in data:
        import capo_application_auto_scaling.types.scaling_policies

        out["scaling_policies"] = (
            capo_application_auto_scaling.types.scaling_policies.deserialize_aws_json_1_1(
                data["ScalingPolicies"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
