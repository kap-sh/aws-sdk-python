"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.send_message_events


class SendMessageResponse(TypedDict):
    events: "aws_sdk_devops_agent.types.send_message_events.SendMessageEvents"
    """<p>The stream of chat message events</p>"""
