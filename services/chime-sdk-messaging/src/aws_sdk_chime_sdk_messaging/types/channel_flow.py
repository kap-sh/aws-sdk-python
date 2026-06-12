"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelFlow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.non_empty_resource_name
    import aws_sdk_chime_sdk_messaging.types.processor_list
    import aws_sdk_chime_sdk_messaging.types.timestamp


class ChannelFlow(TypedDict):
    channel_flow_arn: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the channel flow.</p>"""
    processors: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.processor_list.ProcessorList"
    ]
    """<p>Information about the processor Lambda functions.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the channel flow.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which the channel flow was created.</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a channel flow was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelFlow) -> dict:
    out: dict = {}
    if "channel_flow_arn" in value:
        out["ChannelFlowArn"] = value["channel_flow_arn"]
    if "processors" in value:
        import aws_sdk_chime_sdk_messaging.types.processor_list

        out["Processors"] = (
            aws_sdk_chime_sdk_messaging.types.processor_list.serialize_json(
                value["processors"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["LastUpdatedTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelFlow:
    out: ChannelFlow = {}  # type: ignore[typeddict-item]
    if "ChannelFlowArn" in data:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    if "Processors" in data:
        import aws_sdk_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            aws_sdk_chime_sdk_messaging.types.processor_list.deserialize_json(
                data["Processors"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    return out
