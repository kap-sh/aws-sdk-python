"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPrice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.currency_code
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.route_toll_price_value_range
    import aws_sdk_geo_routes.types.sensitive_boolean
    import aws_sdk_geo_routes.types.sensitive_double


class RouteTollPrice(TypedDict, closed=True):
    currency: "aws_sdk_geo_routes.types.currency_code.CurrencyCode"
    """<p>Currency code corresponding to the price. This is the same as Currency specified in the request.</p>"""
    estimate: "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    """<p>If the price is an estimate or an exact value. </p>"""
    per_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration for which the price corresponds to.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    range: "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    """<p>If the price is a range or an exact value. If any of the toll fares making up the route is a range, the overall price is also a range.</p>"""
    range_value: NotRequired[
        "aws_sdk_geo_routes.types.route_toll_price_value_range.RouteTollPriceValueRange"
    ]
    """<p>Price range with a minimum and maximum value, if a range.</p>"""
    value: "aws_sdk_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Exact price, if not a range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPrice) -> dict:
    out: dict = {}
    out["Currency"] = value["currency"]
    out["Estimate"] = value["estimate"]
    out["PerDuration"] = value.get("per_duration", 0)
    out["Range"] = value["range"]
    if "range_value" in value:
        import aws_sdk_geo_routes.types.route_toll_price_value_range

        out["RangeValue"] = (
            aws_sdk_geo_routes.types.route_toll_price_value_range.serialize_json(
                value["range_value"]
            )
        )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> RouteTollPrice:
    out: RouteTollPrice = {}  # type: ignore[typeddict-item]
    if "Currency" in data:
        out["currency"] = data["Currency"]
    else:
        raise DeserializationError("RouteTollPrice.currency required")
    if "Estimate" in data:
        out["estimate"] = data["Estimate"]
    else:
        raise DeserializationError("RouteTollPrice.estimate required")
    if "PerDuration" in data:
        out["per_duration"] = data["PerDuration"]
    else:
        out["per_duration"] = 0
    if "Range" in data:
        out["range"] = data["Range"]
    else:
        raise DeserializationError("RouteTollPrice.range required")
    if "RangeValue" in data:
        import aws_sdk_geo_routes.types.route_toll_price_value_range

        out["range_value"] = (
            aws_sdk_geo_routes.types.route_toll_price_value_range.deserialize_json(
                data["RangeValue"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("RouteTollPrice.value required")
    return out
