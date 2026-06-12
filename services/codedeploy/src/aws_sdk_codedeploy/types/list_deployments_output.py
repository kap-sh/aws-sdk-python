"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployments_list
    import aws_sdk_codedeploy.types.next_token


class ListDeploymentsOutput(TypedDict):
    deployments: NotRequired[
        "aws_sdk_codedeploy.types.deployments_list.DeploymentsList"
    ]
    """<p>A list of deployment IDs.</p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployments call to return the next set of deployments in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentsOutput) -> dict:
    out: dict = {}
    if "deployments" in value:
        import aws_sdk_codedeploy.types.deployments_list

        out["deployments"] = (
            aws_sdk_codedeploy.types.deployments_list.serialize_aws_json_1_1(
                value["deployments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentsOutput:
    out: ListDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if "deployments" in data:
        import aws_sdk_codedeploy.types.deployments_list

        out["deployments"] = (
            aws_sdk_codedeploy.types.deployments_list.deserialize_aws_json_1_1(
                data["deployments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
