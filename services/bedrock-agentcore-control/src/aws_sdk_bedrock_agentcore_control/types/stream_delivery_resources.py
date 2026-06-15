"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StreamDeliveryResources``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources_list


class StreamDeliveryResources(TypedDict):
    resources: "aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources_list.StreamDeliveryResourcesList"
    """<p>List of stream delivery resource configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamDeliveryResources) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources_list

    out["resources"] = (
        aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources_list.serialize_json(
            value["resources"]
        )
    )
    return out


def deserialize_json(data: dict) -> StreamDeliveryResources:
    out: StreamDeliveryResources = {}  # type: ignore[typeddict-item]
    if "resources" in data:
        import aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources_list

        out["resources"] = (
            aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources_list.deserialize_json(
                data["resources"]
            )
        )
    else:
        raise DeserializationError("StreamDeliveryResources.resources required")
    return out
