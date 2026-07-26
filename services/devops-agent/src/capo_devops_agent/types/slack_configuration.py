"""Generated from Smithy shape ``com.amazonaws.devopsagent#SlackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.slack_transmission_target


class SlackConfiguration(TypedDict, closed=True):
    workspace_id: "str"
    """<p>Associated Slack workspace ID</p>"""
    workspace_name: "str"
    """<p>Associated Slack workspace name</p>"""
    transmission_target: (
        "capo_devops_agent.types.slack_transmission_target.SlackTransmissionTarget"
    )
    """<p>Transmission targets for agent notifications</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackConfiguration) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    out["workspaceName"] = value["workspace_name"]
    import capo_devops_agent.types.slack_transmission_target

    out["transmissionTarget"] = (
        capo_devops_agent.types.slack_transmission_target.serialize_json(
            value["transmission_target"]
        )
    )
    return out


def deserialize_json(data: dict) -> SlackConfiguration:
    out: SlackConfiguration = {}  # type: ignore[typeddict-item]
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("SlackConfiguration.workspace_id required")
    if "workspaceName" in data:
        out["workspace_name"] = data["workspaceName"]
    else:
        raise DeserializationError("SlackConfiguration.workspace_name required")
    if "transmissionTarget" in data:
        import capo_devops_agent.types.slack_transmission_target

        out["transmission_target"] = (
            capo_devops_agent.types.slack_transmission_target.deserialize_json(
                data["transmissionTarget"]
            )
        )
    else:
        raise DeserializationError("SlackConfiguration.transmission_target required")
    return out
