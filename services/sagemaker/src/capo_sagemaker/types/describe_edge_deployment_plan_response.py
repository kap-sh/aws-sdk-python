"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeEdgeDeploymentPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.deployment_stage_status_summaries
    import capo_sagemaker.types.edge_deployment_model_configs
    import capo_sagemaker.types.edge_deployment_plan_arn
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.timestamp


class DescribeEdgeDeploymentPlanResponse(TypedDict, closed=True):
    edge_deployment_plan_arn: NotRequired[
        "capo_sagemaker.types.edge_deployment_plan_arn.EdgeDeploymentPlanArn"
    ]
    """<p>The ARN of edge deployment plan.</p>"""
    edge_deployment_plan_name: NotRequired[
        "capo_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan.</p>"""
    model_configs: NotRequired[
        "capo_sagemaker.types.edge_deployment_model_configs.EdgeDeploymentModelConfigs"
    ]
    """<p>List of models associated with the edge deployment plan.</p>"""
    device_fleet_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The device fleet used for this edge deployment plan.</p>"""
    edge_deployment_success: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The number of edge devices with the successful deployment.</p>"""
    edge_deployment_pending: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The number of edge devices yet to pick up deployment, or in progress.</p>"""
    edge_deployment_failed: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The number of edge devices that failed the deployment.</p>"""
    stages: NotRequired[
        "capo_sagemaker.types.deployment_stage_status_summaries.DeploymentStageStatusSummaries"
    ]
    """<p>List of stages in the edge deployment plan.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>Token to use when calling the next set of stages in the edge deployment plan.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the edge deployment plan was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the edge deployment plan was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEdgeDeploymentPlanResponse) -> dict:
    out: dict = {}
    if "edge_deployment_plan_arn" in value:
        out["EdgeDeploymentPlanArn"] = value["edge_deployment_plan_arn"]
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "model_configs" in value:
        import capo_sagemaker.types.edge_deployment_model_configs

        out["ModelConfigs"] = (
            capo_sagemaker.types.edge_deployment_model_configs.serialize_aws_json_1_1(
                value["model_configs"]
            )
        )
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "edge_deployment_success" in value:
        out["EdgeDeploymentSuccess"] = value["edge_deployment_success"]
    if "edge_deployment_pending" in value:
        out["EdgeDeploymentPending"] = value["edge_deployment_pending"]
    if "edge_deployment_failed" in value:
        out["EdgeDeploymentFailed"] = value["edge_deployment_failed"]
    if "stages" in value:
        import capo_sagemaker.types.deployment_stage_status_summaries

        out["Stages"] = (
            capo_sagemaker.types.deployment_stage_status_summaries.serialize_aws_json_1_1(
                value["stages"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEdgeDeploymentPlanResponse:
    out: DescribeEdgeDeploymentPlanResponse = {}  # type: ignore[typeddict-item]
    if "EdgeDeploymentPlanArn" in data:
        out["edge_deployment_plan_arn"] = data["EdgeDeploymentPlanArn"]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "ModelConfigs" in data:
        import capo_sagemaker.types.edge_deployment_model_configs

        out["model_configs"] = (
            capo_sagemaker.types.edge_deployment_model_configs.deserialize_aws_json_1_1(
                data["ModelConfigs"]
            )
        )
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "EdgeDeploymentSuccess" in data:
        out["edge_deployment_success"] = data["EdgeDeploymentSuccess"]
    if "EdgeDeploymentPending" in data:
        out["edge_deployment_pending"] = data["EdgeDeploymentPending"]
    if "EdgeDeploymentFailed" in data:
        out["edge_deployment_failed"] = data["EdgeDeploymentFailed"]
    if "Stages" in data:
        import capo_sagemaker.types.deployment_stage_status_summaries

        out["stages"] = (
            capo_sagemaker.types.deployment_stage_status_summaries.deserialize_aws_json_1_1(
                data["Stages"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
