"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashPeriodTriggers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.dash_period_trigger

DashPeriodTriggers: TypeAlias = list[
    "capo_mediapackagev2.types.dash_period_trigger.DashPeriodTrigger"
]


# --- restJson1 ser/de ---
def serialize_json(value: DashPeriodTriggers) -> list:
    import capo_mediapackagev2.types.dash_period_trigger

    out: list = []
    for item in value:
        out.append(capo_mediapackagev2.types.dash_period_trigger.serialize_json(item))
    return out


def deserialize_json(data: list) -> DashPeriodTriggers:
    import capo_mediapackagev2.types.dash_period_trigger

    out: DashPeriodTriggers = []
    for item in data:
        out.append(capo_mediapackagev2.types.dash_period_trigger.deserialize_json(item))
    return out
