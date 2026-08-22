"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.event_filter_condition


class SessionFilter(TypedDict, closed=True):
    event_filter: NotRequired[
        "capo_bedrock_agentcore.types.event_filter_condition.EventFilterCondition"
    ]
    """<p>The event filter condition to apply. Use this to filter sessions based on event presence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionFilter) -> dict:
    out: dict = {}
    if "event_filter" in value:
        import capo_bedrock_agentcore.types.event_filter_condition

        out["eventFilter"] = (
            capo_bedrock_agentcore.types.event_filter_condition.serialize_json(
                value["event_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> SessionFilter:
    out: SessionFilter = {}  # type: ignore[typeddict-item]
    if data.get("eventFilter") is not None:
        import capo_bedrock_agentcore.types.event_filter_condition

        out["event_filter"] = (
            capo_bedrock_agentcore.types.event_filter_condition.deserialize_json(
                data["eventFilter"]
            )
        )
    return out
