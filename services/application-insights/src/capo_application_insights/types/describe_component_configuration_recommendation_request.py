"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeComponentConfigurationRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_insights.types.component_name
    import capo_application_insights.types.recommendation_type
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.tier
    import capo_application_insights.types.workload_name


class DescribeComponentConfigurationRecommendationRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: "capo_application_insights.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    tier: "capo_application_insights.types.tier.Tier"
    """<p>The tier of the application component.</p>"""
    workload_name: NotRequired[
        "capo_application_insights.types.workload_name.WorkloadName"
    ]
    """<p>The name of the workload. The name of the workload is required when the tier of the application component is <code>SAP_ASE_SINGLE_NODE</code> or <code>SAP_ASE_HIGH_AVAILABILITY</code>.</p>"""
    recommendation_type: NotRequired[
        "capo_application_insights.types.recommendation_type.RecommendationType"
    ]
    """<p>The recommended configuration type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeComponentConfigurationRecommendationRequest,
) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    import capo_application_insights.types.tier

    out["Tier"] = capo_application_insights.types.tier.serialize_aws_json_1_1(
        value["tier"]
    )
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "recommendation_type" in value:
        import capo_application_insights.types.recommendation_type

        out["RecommendationType"] = (
            capo_application_insights.types.recommendation_type.serialize_aws_json_1_1(
                value["recommendation_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeComponentConfigurationRecommendationRequest:
    out: DescribeComponentConfigurationRecommendationRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError(
            "DescribeComponentConfigurationRecommendationRequest.resource_group_name required"
        )
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    else:
        raise DeserializationError(
            "DescribeComponentConfigurationRecommendationRequest.component_name required"
        )
    if "Tier" in data:
        import capo_application_insights.types.tier

        out["tier"] = capo_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    else:
        raise DeserializationError(
            "DescribeComponentConfigurationRecommendationRequest.tier required"
        )
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    if "RecommendationType" in data:
        import capo_application_insights.types.recommendation_type

        out["recommendation_type"] = (
            capo_application_insights.types.recommendation_type.deserialize_aws_json_1_1(
                data["RecommendationType"]
            )
        )
    return out
