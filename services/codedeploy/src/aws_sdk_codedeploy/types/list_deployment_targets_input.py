"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentTargetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_id
    import aws_sdk_codedeploy.types.next_token
    import aws_sdk_codedeploy.types.target_filters


class ListDeploymentTargetsInput(TypedDict, closed=True):
    deployment_id: "aws_sdk_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p> A token identifier returned from the previous <code>ListDeploymentTargets</code> call. It can be used to return the next set of deployment targets in the list. </p>"""
    target_filters: NotRequired["aws_sdk_codedeploy.types.target_filters.TargetFilters"]
    """<p> A key used to filter the returned targets. The two valid values are:</p> <ul> <li> <p> <code>TargetStatus</code> - A <code>TargetStatus</code> filter string can be <code>Failed</code>, <code>InProgress</code>, <code>Pending</code>, <code>Ready</code>, <code>Skipped</code>, <code>Succeeded</code>, or <code>Unknown</code>. </p> </li> <li> <p> <code>ServerInstanceLabel</code> - A <code>ServerInstanceLabel</code> filter string can be <code>Blue</code> or <code>Green</code>. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentTargetsInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "target_filters" in value:
        import aws_sdk_codedeploy.types.target_filters

        out["targetFilters"] = (
            aws_sdk_codedeploy.types.target_filters.serialize_aws_json_1_1(
                value["target_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentTargetsInput:
    out: ListDeploymentTargetsInput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("ListDeploymentTargetsInput.deployment_id required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "targetFilters" in data:
        import aws_sdk_codedeploy.types.target_filters

        out["target_filters"] = (
            aws_sdk_codedeploy.types.target_filters.deserialize_aws_json_1_1(
                data["targetFilters"]
            )
        )
    return out
