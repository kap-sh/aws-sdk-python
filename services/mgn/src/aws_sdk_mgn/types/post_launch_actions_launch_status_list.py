"""Generated from Smithy shape ``com.amazonaws.mgn#PostLaunchActionsLaunchStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.job_post_launch_actions_launch_status

PostLaunchActionsLaunchStatusList: TypeAlias = list[
    "aws_sdk_mgn.types.job_post_launch_actions_launch_status.JobPostLaunchActionsLaunchStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: PostLaunchActionsLaunchStatusList) -> list:
    import aws_sdk_mgn.types.job_post_launch_actions_launch_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.job_post_launch_actions_launch_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PostLaunchActionsLaunchStatusList:
    import aws_sdk_mgn.types.job_post_launch_actions_launch_status

    out: PostLaunchActionsLaunchStatusList = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.job_post_launch_actions_launch_status.deserialize_json(
                item
            )
        )
    return out
