"""Generated from Smithy shape ``com.amazonaws.mgn#PostLaunchActionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.post_launch_actions_launch_status_list


class PostLaunchActionsStatus(TypedDict):
    ssm_agent_discovery_datetime: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Time where the AWS Systems Manager was detected as running on the Test or Cutover instance.</p>"""
    post_launch_actions_launch_status_list: NotRequired[
        "aws_sdk_mgn.types.post_launch_actions_launch_status_list.PostLaunchActionsLaunchStatusList"
    ]
    """<p>List of Post Launch Action status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostLaunchActionsStatus) -> dict:
    out: dict = {}
    if "ssm_agent_discovery_datetime" in value:
        out["ssmAgentDiscoveryDatetime"] = value["ssm_agent_discovery_datetime"]
    if "post_launch_actions_launch_status_list" in value:
        import aws_sdk_mgn.types.post_launch_actions_launch_status_list

        out["postLaunchActionsLaunchStatusList"] = (
            aws_sdk_mgn.types.post_launch_actions_launch_status_list.serialize_json(
                value["post_launch_actions_launch_status_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> PostLaunchActionsStatus:
    out: PostLaunchActionsStatus = {}  # type: ignore[typeddict-item]
    if "ssmAgentDiscoveryDatetime" in data:
        out["ssm_agent_discovery_datetime"] = data["ssmAgentDiscoveryDatetime"]
    if "postLaunchActionsLaunchStatusList" in data:
        import aws_sdk_mgn.types.post_launch_actions_launch_status_list

        out["post_launch_actions_launch_status_list"] = (
            aws_sdk_mgn.types.post_launch_actions_launch_status_list.deserialize_json(
                data["postLaunchActionsLaunchStatusList"]
            )
        )
    return out
