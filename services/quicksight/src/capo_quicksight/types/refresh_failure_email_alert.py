"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshFailureEmailAlert``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.refresh_failure_alert_status


class RefreshFailureEmailAlert(TypedDict, closed=True):
    alert_status: NotRequired[
        "capo_quicksight.types.refresh_failure_alert_status.RefreshFailureAlertStatus"
    ]
    """<p>The status value that determines if email alerts are sent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshFailureEmailAlert) -> dict:
    out: dict = {}
    if "alert_status" in value:
        import capo_quicksight.types.refresh_failure_alert_status

        out["AlertStatus"] = (
            capo_quicksight.types.refresh_failure_alert_status.serialize_json(
                value["alert_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> RefreshFailureEmailAlert:
    out: RefreshFailureEmailAlert = {}  # type: ignore[typeddict-item]
    if "AlertStatus" in data:
        import capo_quicksight.types.refresh_failure_alert_status

        out["alert_status"] = (
            capo_quicksight.types.refresh_failure_alert_status.deserialize_json(
                data["AlertStatus"]
            )
        )
    return out
