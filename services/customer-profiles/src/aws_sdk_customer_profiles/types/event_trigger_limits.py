"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.optional_long
    import aws_sdk_customer_profiles.types.periods


class EventTriggerLimits(TypedDict, closed=True):
    event_expiration: NotRequired[
        "aws_sdk_customer_profiles.types.optional_long.optionalLong"
    ]
    """<p>In milliseconds. Specifies that an event will only trigger the destination if it is processed within a certain latency period.</p>"""
    periods: NotRequired["aws_sdk_customer_profiles.types.periods.Periods"]
    """<p>A list of time periods during which the limits apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerLimits) -> dict:
    out: dict = {}
    if "event_expiration" in value:
        out["EventExpiration"] = value["event_expiration"]
    if "periods" in value:
        import aws_sdk_customer_profiles.types.periods

        out["Periods"] = aws_sdk_customer_profiles.types.periods.serialize_json(
            value["periods"]
        )
    return out


def deserialize_json(data: dict) -> EventTriggerLimits:
    out: EventTriggerLimits = {}  # type: ignore[typeddict-item]
    if "EventExpiration" in data:
        out["event_expiration"] = data["EventExpiration"]
    if "Periods" in data:
        import aws_sdk_customer_profiles.types.periods

        out["periods"] = aws_sdk_customer_profiles.types.periods.deserialize_json(
            data["Periods"]
        )
    return out
