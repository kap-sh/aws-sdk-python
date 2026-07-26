"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateScheduledActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.scheduled_action


class UpdateScheduledActionResponse(TypedDict, closed=True):
    scheduled_action: NotRequired[
        "capo_opensearch.types.scheduled_action.ScheduledAction"
    ]
    """<p>Information about the rescheduled action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScheduledActionResponse) -> dict:
    out: dict = {}
    if "scheduled_action" in value:
        import capo_opensearch.types.scheduled_action

        out["ScheduledAction"] = capo_opensearch.types.scheduled_action.serialize_json(
            value["scheduled_action"]
        )
    return out


def deserialize_json(data: dict) -> UpdateScheduledActionResponse:
    out: UpdateScheduledActionResponse = {}  # type: ignore[typeddict-item]
    if "ScheduledAction" in data:
        import capo_opensearch.types.scheduled_action

        out["scheduled_action"] = (
            capo_opensearch.types.scheduled_action.deserialize_json(
                data["ScheduledAction"]
            )
        )
    return out
