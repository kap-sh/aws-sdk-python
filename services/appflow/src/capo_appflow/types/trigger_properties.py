"""Generated from Smithy shape ``com.amazonaws.appflow#TriggerProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.scheduled_trigger_properties


class TriggerProperties(TypedDict, closed=True):
    scheduled: NotRequired[
        "capo_appflow.types.scheduled_trigger_properties.ScheduledTriggerProperties"
    ]
    """<p> Specifies the configuration details of a schedule-triggered flow as defined by the user. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerProperties) -> dict:
    out: dict = {}
    if "scheduled" in value:
        import capo_appflow.types.scheduled_trigger_properties

        out["Scheduled"] = (
            capo_appflow.types.scheduled_trigger_properties.serialize_json(
                value["scheduled"]
            )
        )
    return out


def deserialize_json(data: dict) -> TriggerProperties:
    out: TriggerProperties = {}  # type: ignore[typeddict-item]
    if "Scheduled" in data:
        import capo_appflow.types.scheduled_trigger_properties

        out["scheduled"] = (
            capo_appflow.types.scheduled_trigger_properties.deserialize_json(
                data["Scheduled"]
            )
        )
    return out
