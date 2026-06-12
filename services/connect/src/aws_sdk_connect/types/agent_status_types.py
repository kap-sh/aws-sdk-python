"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_type

AgentStatusTypes: TypeAlias = list[
    "aws_sdk_connect.types.agent_status_type.AgentStatusType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusTypes) -> list:
    import aws_sdk_connect.types.agent_status_type

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.agent_status_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentStatusTypes:
    import aws_sdk_connect.types.agent_status_type

    out: AgentStatusTypes = []
    for item in data:
        out.append(aws_sdk_connect.types.agent_status_type.deserialize_json(item))
    return out
