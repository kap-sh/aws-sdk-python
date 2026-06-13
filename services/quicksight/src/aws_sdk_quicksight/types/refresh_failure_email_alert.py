"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshFailureEmailAlert``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.refresh_failure_alert_status


class RefreshFailureEmailAlert(TypedDict):
    alert_status: NotRequired[
        "aws_sdk_quicksight.types.refresh_failure_alert_status.RefreshFailureAlertStatus"
    ]
    """<p>The status value that determines if email alerts are sent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshFailureEmailAlert) -> dict:
    out: dict = {}
    if "alert_status" in value:
        import aws_sdk_quicksight.types.refresh_failure_alert_status

        out["AlertStatus"] = (
            aws_sdk_quicksight.types.refresh_failure_alert_status.serialize_json(
                value["alert_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> RefreshFailureEmailAlert:
    out: RefreshFailureEmailAlert = {}  # type: ignore[typeddict-item]
    if "AlertStatus" in data:
        import aws_sdk_quicksight.types.refresh_failure_alert_status

        out["alert_status"] = (
            aws_sdk_quicksight.types.refresh_failure_alert_status.deserialize_json(
                data["AlertStatus"]
            )
        )
    return out
