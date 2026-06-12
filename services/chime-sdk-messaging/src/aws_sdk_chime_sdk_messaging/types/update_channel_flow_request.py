"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.non_empty_resource_name
    import aws_sdk_chime_sdk_messaging.types.processor_list


class UpdateChannelFlowRequest(TypedDict):
    channel_flow_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow.</p>"""
    processors: "aws_sdk_chime_sdk_messaging.types.processor_list.ProcessorList"
    """<p>Information about the processor Lambda functions </p>"""
    name: (
        "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    )
    """<p>The name of the channel flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelFlowRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_messaging.types.processor_list

    out["Processors"] = aws_sdk_chime_sdk_messaging.types.processor_list.serialize_json(
        value["processors"]
    )
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateChannelFlowRequest:
    out: UpdateChannelFlowRequest = {}  # type: ignore[typeddict-item]
    if "Processors" in data:
        import aws_sdk_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            aws_sdk_chime_sdk_messaging.types.processor_list.deserialize_json(
                data["Processors"]
            )
        )
    else:
        raise DeserializationError("UpdateChannelFlowRequest.processors required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateChannelFlowRequest.name required")
    return out
