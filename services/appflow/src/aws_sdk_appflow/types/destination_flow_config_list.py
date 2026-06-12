"""Generated from Smithy shape ``com.amazonaws.appflow#DestinationFlowConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.destination_flow_config

DestinationFlowConfigList: TypeAlias = list[
    "aws_sdk_appflow.types.destination_flow_config.DestinationFlowConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationFlowConfigList) -> list:
    import aws_sdk_appflow.types.destination_flow_config

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.destination_flow_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> DestinationFlowConfigList:
    import aws_sdk_appflow.types.destination_flow_config

    out: DestinationFlowConfigList = []
    for item in data:
        out.append(aws_sdk_appflow.types.destination_flow_config.deserialize_json(item))
    return out
