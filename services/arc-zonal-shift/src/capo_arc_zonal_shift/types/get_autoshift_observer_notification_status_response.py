"""Generated from Smithy shape ``com.amazonaws.arczonalshift#GetAutoshiftObserverNotificationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.autoshift_observer_notification_status


class GetAutoshiftObserverNotificationStatusResponse(TypedDict, closed=True):
    status: "capo_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus"
    """<p>The status of autoshift observer notification. If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the Amazon EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutoshiftObserverNotificationStatusResponse) -> dict:
    out: dict = {}
    import capo_arc_zonal_shift.types.autoshift_observer_notification_status

    out["status"] = (
        capo_arc_zonal_shift.types.autoshift_observer_notification_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAutoshiftObserverNotificationStatusResponse:
    out: GetAutoshiftObserverNotificationStatusResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_arc_zonal_shift.types.autoshift_observer_notification_status

        out["status"] = (
            capo_arc_zonal_shift.types.autoshift_observer_notification_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutoshiftObserverNotificationStatusResponse.status required"
        )
    return out
