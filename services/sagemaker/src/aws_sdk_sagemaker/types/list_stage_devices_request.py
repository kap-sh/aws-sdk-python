"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListStageDevicesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.list_max_results
    import aws_sdk_sagemaker.types.next_token


class ListStageDevicesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>The response from the last list when returning a list large enough to neeed tokening.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.list_max_results.ListMaxResults"]
    """<p>The maximum number of requests to select.</p>"""
    edge_deployment_plan_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge deployment plan.</p>"""
    exclude_devices_deployed_in_other_stage: NotRequired[
        "aws_sdk_sagemaker.types.boolean.Boolean"
    ]
    """<p>Toggle for excluding devices deployed in other stages.</p>"""
    stage_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the stage in the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStageDevicesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "edge_deployment_plan_name" in value:
        out["EdgeDeploymentPlanName"] = value["edge_deployment_plan_name"]
    if "exclude_devices_deployed_in_other_stage" in value:
        out["ExcludeDevicesDeployedInOtherStage"] = value[
            "exclude_devices_deployed_in_other_stage"
        ]
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStageDevicesRequest:
    out: ListStageDevicesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "EdgeDeploymentPlanName" in data:
        out["edge_deployment_plan_name"] = data["EdgeDeploymentPlanName"]
    if "ExcludeDevicesDeployedInOtherStage" in data:
        out["exclude_devices_deployed_in_other_stage"] = data[
            "ExcludeDevicesDeployedInOtherStage"
        ]
    if "StageName" in data:
        out["stage_name"] = data["StageName"]
    return out
