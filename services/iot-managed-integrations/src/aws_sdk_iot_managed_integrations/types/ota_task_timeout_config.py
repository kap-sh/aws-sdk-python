"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskTimeoutConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.in_progress_timeout_in_minutes


class OtaTaskTimeoutConfig(TypedDict, closed=True):
    in_progress_timeout_in_minutes: NotRequired[
        "aws_sdk_iot_managed_integrations.types.in_progress_timeout_in_minutes.InProgressTimeoutInMinutes"
    ]
    """<p>Specifies the amount of time the device has to finish execution of this task. The timeout interval can be anywhere between 1 minute and 7 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskTimeoutConfig) -> dict:
    out: dict = {}
    if "in_progress_timeout_in_minutes" in value:
        out["InProgressTimeoutInMinutes"] = value["in_progress_timeout_in_minutes"]
    return out


def deserialize_json(data: dict) -> OtaTaskTimeoutConfig:
    out: OtaTaskTimeoutConfig = {}  # type: ignore[typeddict-item]
    if "InProgressTimeoutInMinutes" in data:
        out["in_progress_timeout_in_minutes"] = data["InProgressTimeoutInMinutes"]
    return out
