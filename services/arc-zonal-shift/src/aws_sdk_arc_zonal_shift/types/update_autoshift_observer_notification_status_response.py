"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdateAutoshiftObserverNotificationStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status


class UpdateAutoshiftObserverNotificationStatusResponse(TypedDict):
    status: "aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus"
    """<p>The status for autoshift observer notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutoshiftObserverNotificationStatusResponse) -> dict:
    out: dict = {}
    import aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status

    out["status"] = (
        aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAutoshiftObserverNotificationStatusResponse:
    out: UpdateAutoshiftObserverNotificationStatusResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status

        out["status"] = (
            aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAutoshiftObserverNotificationStatusResponse.status required"
        )
    return out
