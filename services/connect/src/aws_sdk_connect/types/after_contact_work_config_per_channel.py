"""Generated from Smithy shape ``com.amazonaws.connect#AfterContactWorkConfigPerChannel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.after_contact_work_config
    import aws_sdk_connect.types.channel


class AfterContactWorkConfigPerChannel(TypedDict):
    channel: "aws_sdk_connect.types.channel.Channel"
    """<p>The channel for this ACW timeout configuration. Valid values: VOICE, CHAT, TASK, EMAIL.</p>"""
    after_contact_work_config: (
        "aws_sdk_connect.types.after_contact_work_config.AfterContactWorkConfig"
    )
    """<p>The ACW timeout settings for this channel.</p>"""
    agent_first_callback_after_contact_work_config: NotRequired[
        "aws_sdk_connect.types.after_contact_work_config.AfterContactWorkConfig"
    ]
    """<p>The ACW timeout settings for agent-first callbacks. This setting only applies to the VOICE channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AfterContactWorkConfigPerChannel) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.channel

    out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    import aws_sdk_connect.types.after_contact_work_config

    out["AfterContactWorkConfig"] = (
        aws_sdk_connect.types.after_contact_work_config.serialize_json(
            value["after_contact_work_config"]
        )
    )
    if "agent_first_callback_after_contact_work_config" in value:
        import aws_sdk_connect.types.after_contact_work_config

        out["AgentFirstCallbackAfterContactWorkConfig"] = (
            aws_sdk_connect.types.after_contact_work_config.serialize_json(
                value["agent_first_callback_after_contact_work_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AfterContactWorkConfigPerChannel:
    out: AfterContactWorkConfigPerChannel = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("AfterContactWorkConfigPerChannel.channel required")
    if "AfterContactWorkConfig" in data:
        import aws_sdk_connect.types.after_contact_work_config

        out["after_contact_work_config"] = (
            aws_sdk_connect.types.after_contact_work_config.deserialize_json(
                data["AfterContactWorkConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AfterContactWorkConfigPerChannel.after_contact_work_config required"
        )
    if "AgentFirstCallbackAfterContactWorkConfig" in data:
        import aws_sdk_connect.types.after_contact_work_config

        out["agent_first_callback_after_contact_work_config"] = (
            aws_sdk_connect.types.after_contact_work_config.deserialize_json(
                data["AgentFirstCallbackAfterContactWorkConfig"]
            )
        )
    return out
