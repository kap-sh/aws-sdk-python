"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdateAutoshiftObserverNotificationStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status


class UpdateAutoshiftObserverNotificationStatusRequest(TypedDict):
    status: "aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus"
    """<p>The status to set for autoshift observer notification. If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the Amazon EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutoshiftObserverNotificationStatusRequest) -> dict:
    out: dict = {}
    import aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status

    out["status"] = (
        aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAutoshiftObserverNotificationStatusRequest:
    out: UpdateAutoshiftObserverNotificationStatusRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status

        out["status"] = (
            aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAutoshiftObserverNotificationStatusRequest.status required"
        )
    return out
