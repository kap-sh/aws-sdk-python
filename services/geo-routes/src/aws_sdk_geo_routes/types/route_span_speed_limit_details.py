"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanSpeedLimitDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_boolean
    import aws_sdk_geo_routes.types.speed_kilometers_per_hour


class RouteSpanSpeedLimitDetails(TypedDict, closed=True):
    max_speed: (
        "aws_sdk_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    )
    """<p>Maximum speed.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    unlimited: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>If the span doesn't have a speed limit like the Autobahn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanSpeedLimitDetails) -> dict:
    out: dict = {}
    out["MaxSpeed"] = value.get("max_speed", 0)
    if "unlimited" in value:
        out["Unlimited"] = value["unlimited"]
    return out


def deserialize_json(data: dict) -> RouteSpanSpeedLimitDetails:
    out: RouteSpanSpeedLimitDetails = {}  # type: ignore[typeddict-item]
    if "MaxSpeed" in data:
        out["max_speed"] = data["MaxSpeed"]
    else:
        out["max_speed"] = 0
    if "Unlimited" in data:
        out["unlimited"] = data["Unlimited"]
    return out
