"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListDeploymentEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_event_data_summary_list
    import capo_launch_wizard.types.next_token


class ListDeploymentEventsOutput(TypedDict, closed=True):
    deployment_events: NotRequired[
        "capo_launch_wizard.types.deployment_event_data_summary_list.DeploymentEventDataSummaryList"
    ]
    """<p>Lists the deployment events.</p>"""
    next_token: NotRequired["capo_launch_wizard.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentEventsOutput) -> dict:
    out: dict = {}
    if "deployment_events" in value:
        import capo_launch_wizard.types.deployment_event_data_summary_list

        out["deploymentEvents"] = (
            capo_launch_wizard.types.deployment_event_data_summary_list.serialize_json(
                value["deployment_events"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeploymentEventsOutput:
    out: ListDeploymentEventsOutput = {}  # type: ignore[typeddict-item]
    if "deploymentEvents" in data:
        import capo_launch_wizard.types.deployment_event_data_summary_list

        out["deployment_events"] = (
            capo_launch_wizard.types.deployment_event_data_summary_list.deserialize_json(
                data["deploymentEvents"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
