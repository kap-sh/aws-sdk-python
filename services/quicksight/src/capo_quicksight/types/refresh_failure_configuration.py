"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshFailureConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.refresh_failure_email_alert


class RefreshFailureConfiguration(TypedDict, closed=True):
    email_alert: NotRequired[
        "capo_quicksight.types.refresh_failure_email_alert.RefreshFailureEmailAlert"
    ]
    """<p>The email alert configuration for a dataset refresh failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshFailureConfiguration) -> dict:
    out: dict = {}
    if "email_alert" in value:
        import capo_quicksight.types.refresh_failure_email_alert

        out["EmailAlert"] = (
            capo_quicksight.types.refresh_failure_email_alert.serialize_json(
                value["email_alert"]
            )
        )
    return out


def deserialize_json(data: dict) -> RefreshFailureConfiguration:
    out: RefreshFailureConfiguration = {}  # type: ignore[typeddict-item]
    if "EmailAlert" in data:
        import capo_quicksight.types.refresh_failure_email_alert

        out["email_alert"] = (
            capo_quicksight.types.refresh_failure_email_alert.deserialize_json(
                data["EmailAlert"]
            )
        )
    return out
