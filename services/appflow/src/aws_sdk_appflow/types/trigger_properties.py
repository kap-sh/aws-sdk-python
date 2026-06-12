"""Generated from Smithy shape ``com.amazonaws.appflow#TriggerProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.scheduled_trigger_properties


class TriggerProperties(TypedDict):
    scheduled: NotRequired[
        "aws_sdk_appflow.types.scheduled_trigger_properties.ScheduledTriggerProperties"
    ]
    """<p> Specifies the configuration details of a schedule-triggered flow as defined by the user. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerProperties) -> dict:
    out: dict = {}
    if "scheduled" in value:
        import aws_sdk_appflow.types.scheduled_trigger_properties

        out["Scheduled"] = (
            aws_sdk_appflow.types.scheduled_trigger_properties.serialize_json(
                value["scheduled"]
            )
        )
    return out


def deserialize_json(data: dict) -> TriggerProperties:
    out: TriggerProperties = {}  # type: ignore[typeddict-item]
    if "Scheduled" in data:
        import aws_sdk_appflow.types.scheduled_trigger_properties

        out["scheduled"] = (
            aws_sdk_appflow.types.scheduled_trigger_properties.deserialize_json(
                data["Scheduled"]
            )
        )
    return out
