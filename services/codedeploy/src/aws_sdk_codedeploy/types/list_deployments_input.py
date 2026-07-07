"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.deployment_group_name
    import aws_sdk_codedeploy.types.deployment_status_list
    import aws_sdk_codedeploy.types.external_id
    import aws_sdk_codedeploy.types.next_token
    import aws_sdk_codedeploy.types.time_range


class ListDeploymentsInput(TypedDict, closed=True):
    application_name: NotRequired[
        "aws_sdk_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p> <note> <p>If <code>applicationName</code> is specified, then <code>deploymentGroupName</code> must be specified. If it is not specified, then <code>deploymentGroupName</code> must not be specified. </p> </note>"""
    deployment_group_name: NotRequired[
        "aws_sdk_codedeploy.types.deployment_group_name.DeploymentGroupName"
    ]
    """<p>The name of a deployment group for the specified application.</p> <note> <p>If <code>deploymentGroupName</code> is specified, then <code>applicationName</code> must be specified. If it is not specified, then <code>applicationName</code> must not be specified. </p> </note>"""
    external_id: NotRequired["aws_sdk_codedeploy.types.external_id.ExternalId"]
    """<p>The unique ID of an external resource for returning deployments linked to the external resource.</p>"""
    include_only_statuses: NotRequired[
        "aws_sdk_codedeploy.types.deployment_status_list.DeploymentStatusList"
    ]
    """<p>A subset of deployments to list by status:</p> <ul> <li> <p> <code>Created</code>: Include created deployments in the resulting list.</p> </li> <li> <p> <code>Queued</code>: Include queued deployments in the resulting list.</p> </li> <li> <p> <code>In Progress</code>: Include in-progress deployments in the resulting list.</p> </li> <li> <p> <code>Succeeded</code>: Include successful deployments in the resulting list.</p> </li> <li> <p> <code>Failed</code>: Include failed deployments in the resulting list.</p> </li> <li> <p> <code>Stopped</code>: Include stopped deployments in the resulting list.</p> </li> </ul>"""
    create_time_range: NotRequired["aws_sdk_codedeploy.types.time_range.TimeRange"]
    """<p>A time range (start and end) for returning a subset of the list of deployments.</p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>An identifier returned from the previous list deployments call. It can be used to return the next set of deployments in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentsInput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "deployment_group_name" in value:
        out["deploymentGroupName"] = value["deployment_group_name"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "include_only_statuses" in value:
        import aws_sdk_codedeploy.types.deployment_status_list

        out["includeOnlyStatuses"] = (
            aws_sdk_codedeploy.types.deployment_status_list.serialize_aws_json_1_1(
                value["include_only_statuses"]
            )
        )
    if "create_time_range" in value:
        import aws_sdk_codedeploy.types.time_range

        out["createTimeRange"] = (
            aws_sdk_codedeploy.types.time_range.serialize_aws_json_1_1(
                value["create_time_range"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentsInput:
    out: ListDeploymentsInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    if "deploymentGroupName" in data:
        out["deployment_group_name"] = data["deploymentGroupName"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "includeOnlyStatuses" in data:
        import aws_sdk_codedeploy.types.deployment_status_list

        out["include_only_statuses"] = (
            aws_sdk_codedeploy.types.deployment_status_list.deserialize_aws_json_1_1(
                data["includeOnlyStatuses"]
            )
        )
    if "createTimeRange" in data:
        import aws_sdk_codedeploy.types.time_range

        out["create_time_range"] = (
            aws_sdk_codedeploy.types.time_range.deserialize_aws_json_1_1(
                data["createTimeRange"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
