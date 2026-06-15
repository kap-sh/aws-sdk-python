"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.event_filter_condition


class SessionFilter(TypedDict):
    event_filter: NotRequired[
        "aws_sdk_bedrock_agentcore.types.event_filter_condition.EventFilterCondition"
    ]
    """<p>The event filter condition to apply. Use this to filter sessions based on event presence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionFilter) -> dict:
    out: dict = {}
    if "event_filter" in value:
        import aws_sdk_bedrock_agentcore.types.event_filter_condition

        out["eventFilter"] = (
            aws_sdk_bedrock_agentcore.types.event_filter_condition.serialize_json(
                value["event_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> SessionFilter:
    out: SessionFilter = {}  # type: ignore[typeddict-item]
    if "eventFilter" in data:
        import aws_sdk_bedrock_agentcore.types.event_filter_condition

        out["event_filter"] = (
            aws_sdk_bedrock_agentcore.types.event_filter_condition.deserialize_json(
                data["eventFilter"]
            )
        )
    return out
