"""Generated from Smithy shape ``com.amazonaws.inspector#AgentHealthCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_health_code

AgentHealthCodeList: TypeAlias = list[
    "aws_sdk_inspector.types.agent_health_code.AgentHealthCode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentHealthCodeList) -> list:
    import aws_sdk_inspector.types.agent_health_code

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.agent_health_code.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AgentHealthCodeList:
    import aws_sdk_inspector.types.agent_health_code

    out: AgentHealthCodeList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.agent_health_code.deserialize_aws_json_1_1(item)
        )
    return out
