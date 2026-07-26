"""Generated from Smithy shape ``com.amazonaws.connect#OverrideHour``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.common_human_readable_name
    import capo_connect.types.operational_status
    import capo_connect.types.override_time_slice


class OverrideHour(TypedDict, closed=True):
    start: NotRequired["capo_connect.types.override_time_slice.OverrideTimeSlice"]
    end: NotRequired["capo_connect.types.override_time_slice.OverrideTimeSlice"]
    override_name: NotRequired[
        "capo_connect.types.common_human_readable_name.CommonHumanReadableName"
    ]
    """<p>Unique identifier name for the override.</p>"""
    operational_status: NotRequired[
        "capo_connect.types.operational_status.OperationalStatus"
    ]
    """<p>Indicates whether the status is open or closed during the override period. This status determines how the override modifies the base hours of operation schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverrideHour) -> dict:
    out: dict = {}
    if "start" in value:
        import capo_connect.types.override_time_slice

        out["Start"] = capo_connect.types.override_time_slice.serialize_json(
            value["start"]
        )
    if "end" in value:
        import capo_connect.types.override_time_slice

        out["End"] = capo_connect.types.override_time_slice.serialize_json(value["end"])
    if "override_name" in value:
        out["OverrideName"] = value["override_name"]
    if "operational_status" in value:
        import capo_connect.types.operational_status

        out["OperationalStatus"] = capo_connect.types.operational_status.serialize_json(
            value["operational_status"]
        )
    return out


def deserialize_json(data: dict) -> OverrideHour:
    out: OverrideHour = {}  # type: ignore[typeddict-item]
    if "Start" in data:
        import capo_connect.types.override_time_slice

        out["start"] = capo_connect.types.override_time_slice.deserialize_json(
            data["Start"]
        )
    if "End" in data:
        import capo_connect.types.override_time_slice

        out["end"] = capo_connect.types.override_time_slice.deserialize_json(
            data["End"]
        )
    if "OverrideName" in data:
        out["override_name"] = data["OverrideName"]
    if "OperationalStatus" in data:
        import capo_connect.types.operational_status

        out["operational_status"] = (
            capo_connect.types.operational_status.deserialize_json(
                data["OperationalStatus"]
            )
        )
    return out
