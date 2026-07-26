"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeDeploymentPlanSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_deployment_plan_summary

EdgeDeploymentPlanSummaries: TypeAlias = list[
    "capo_sagemaker.types.edge_deployment_plan_summary.EdgeDeploymentPlanSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeDeploymentPlanSummaries) -> list:
    import capo_sagemaker.types.edge_deployment_plan_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.edge_deployment_plan_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EdgeDeploymentPlanSummaries:
    import capo_sagemaker.types.edge_deployment_plan_summary

    out: EdgeDeploymentPlanSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.edge_deployment_plan_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
