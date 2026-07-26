"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TriggerProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.scheduled_trigger_properties


class TriggerProperties(TypedDict, closed=True):
    scheduled: NotRequired[
        "capo_customer_profiles.types.scheduled_trigger_properties.ScheduledTriggerProperties"
    ]
    """<p>Specifies the configuration details of a schedule-triggered flow that you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerProperties) -> dict:
    out: dict = {}
    if "scheduled" in value:
        import capo_customer_profiles.types.scheduled_trigger_properties

        out["Scheduled"] = (
            capo_customer_profiles.types.scheduled_trigger_properties.serialize_json(
                value["scheduled"]
            )
        )
    return out


def deserialize_json(data: dict) -> TriggerProperties:
    out: TriggerProperties = {}  # type: ignore[typeddict-item]
    if "Scheduled" in data:
        import capo_customer_profiles.types.scheduled_trigger_properties

        out["scheduled"] = (
            capo_customer_profiles.types.scheduled_trigger_properties.deserialize_json(
                data["Scheduled"]
            )
        )
    return out
