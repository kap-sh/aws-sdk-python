"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BurnRateConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.burn_rate_look_back_window_minutes


class BurnRateConfiguration(TypedDict):
    look_back_window_minutes: "aws_sdk_application_signals.types.burn_rate_look_back_window_minutes.BurnRateLookBackWindowMinutes"
    """<p>The number of minutes to use as the look-back window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BurnRateConfiguration) -> dict:
    out: dict = {}
    out["LookBackWindowMinutes"] = value["look_back_window_minutes"]
    return out


def deserialize_json(data: dict) -> BurnRateConfiguration:
    out: BurnRateConfiguration = {}  # type: ignore[typeddict-item]
    if "LookBackWindowMinutes" in data:
        out["look_back_window_minutes"] = data["LookBackWindowMinutes"]
    else:
        raise DeserializationError(
            "BurnRateConfiguration.look_back_window_minutes required"
        )
    return out
