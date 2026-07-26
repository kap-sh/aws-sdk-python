"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowExecutionMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_execution_message

FlowExecutionMessages: TypeAlias = list[
    "capo_iotthingsgraph.types.flow_execution_message.FlowExecutionMessage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowExecutionMessages) -> list:
    import capo_iotthingsgraph.types.flow_execution_message

    out: list = []
    for item in value:
        out.append(
            capo_iotthingsgraph.types.flow_execution_message.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FlowExecutionMessages:
    import capo_iotthingsgraph.types.flow_execution_message

    out: FlowExecutionMessages = []
    for item in data:
        out.append(
            capo_iotthingsgraph.types.flow_execution_message.deserialize_aws_json_1_1(
                item
            )
        )
    return out
