"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelFlowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.non_empty_resource_name
    import aws_sdk_chime_sdk_messaging.types.processor_list


class ChannelFlowSummary(TypedDict, closed=True):
    channel_flow_arn: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the channel flow.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the channel flow.</p>"""
    processors: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.processor_list.ProcessorList"
    ]
    """<p>Information about the processor Lambda functions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelFlowSummary) -> dict:
    out: dict = {}
    if "channel_flow_arn" in value:
        out["ChannelFlowArn"] = value["channel_flow_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "processors" in value:
        import aws_sdk_chime_sdk_messaging.types.processor_list

        out["Processors"] = (
            aws_sdk_chime_sdk_messaging.types.processor_list.serialize_json(
                value["processors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelFlowSummary:
    out: ChannelFlowSummary = {}  # type: ignore[typeddict-item]
    if "ChannelFlowArn" in data:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Processors" in data:
        import aws_sdk_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            aws_sdk_chime_sdk_messaging.types.processor_list.deserialize_json(
                data["Processors"]
            )
        )
    return out
