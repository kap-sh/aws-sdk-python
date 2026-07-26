"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.scheduled_auto_tune_details


class AutoTuneDetails(TypedDict, closed=True):
    scheduled_auto_tune_details: NotRequired[
        "capo_opensearch.types.scheduled_auto_tune_details.ScheduledAutoTuneDetails"
    ]
    """<p>Container for details about a scheduled Auto-Tune action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneDetails) -> dict:
    out: dict = {}
    if "scheduled_auto_tune_details" in value:
        import capo_opensearch.types.scheduled_auto_tune_details

        out["ScheduledAutoTuneDetails"] = (
            capo_opensearch.types.scheduled_auto_tune_details.serialize_json(
                value["scheduled_auto_tune_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoTuneDetails:
    out: AutoTuneDetails = {}  # type: ignore[typeddict-item]
    if "ScheduledAutoTuneDetails" in data:
        import capo_opensearch.types.scheduled_auto_tune_details

        out["scheduled_auto_tune_details"] = (
            capo_opensearch.types.scheduled_auto_tune_details.deserialize_json(
                data["ScheduledAutoTuneDetails"]
            )
        )
    return out
