"""Generated from Smithy shape ``com.amazonaws.devopsagent#EventChannelDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.event_channel_type


class EventChannelDetails(TypedDict, closed=True):
    type: NotRequired["capo_devops_agent.types.event_channel_type.EventChannelType"]
    """<p>The type of event channel</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventChannelDetails) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_devops_agent.types.event_channel_type

        out["type"] = capo_devops_agent.types.event_channel_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> EventChannelDetails:
    out: EventChannelDetails = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_devops_agent.types.event_channel_type

        out["type"] = capo_devops_agent.types.event_channel_type.deserialize_json(
            data["type"]
        )
    return out
