"""Generated from Smithy shape ``com.amazonaws.workmail#DeviceUserAgentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.device_user_agent

DeviceUserAgentList: TypeAlias = list[
    "capo_workmail.types.device_user_agent.DeviceUserAgent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceUserAgentList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeviceUserAgentList:
    return list(data)
