"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListDeploymentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_data_summary_list
    import aws_sdk_launch_wizard.types.next_token


class ListDeploymentsOutput(TypedDict, closed=True):
    deployments: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_data_summary_list.DeploymentDataSummaryList"
    ]
    """<p>Lists the deployments.</p>"""
    next_token: NotRequired["aws_sdk_launch_wizard.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentsOutput) -> dict:
    out: dict = {}
    if "deployments" in value:
        import aws_sdk_launch_wizard.types.deployment_data_summary_list

        out["deployments"] = (
            aws_sdk_launch_wizard.types.deployment_data_summary_list.serialize_json(
                value["deployments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeploymentsOutput:
    out: ListDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if "deployments" in data:
        import aws_sdk_launch_wizard.types.deployment_data_summary_list

        out["deployments"] = (
            aws_sdk_launch_wizard.types.deployment_data_summary_list.deserialize_json(
                data["deployments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
