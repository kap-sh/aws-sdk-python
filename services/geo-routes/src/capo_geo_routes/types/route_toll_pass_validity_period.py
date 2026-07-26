"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPassValidityPeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_toll_pass_validity_period_type
    import capo_geo_routes.types.sensitive_integer


class RouteTollPassValidityPeriod(TypedDict, closed=True):
    period: "capo_geo_routes.types.route_toll_pass_validity_period_type.RouteTollPassValidityPeriodType"
    """<p>Validity period.</p>"""
    period_count: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Counts for the validity period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPassValidityPeriod) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_toll_pass_validity_period_type

    out["Period"] = (
        capo_geo_routes.types.route_toll_pass_validity_period_type.serialize_json(
            value["period"]
        )
    )
    if "period_count" in value:
        out["PeriodCount"] = value["period_count"]
    return out


def deserialize_json(data: dict) -> RouteTollPassValidityPeriod:
    out: RouteTollPassValidityPeriod = {}  # type: ignore[typeddict-item]
    if "Period" in data:
        import capo_geo_routes.types.route_toll_pass_validity_period_type

        out["period"] = (
            capo_geo_routes.types.route_toll_pass_validity_period_type.deserialize_json(
                data["Period"]
            )
        )
    else:
        raise DeserializationError("RouteTollPassValidityPeriod.period required")
    if "PeriodCount" in data:
        out["period_count"] = data["PeriodCount"]
    return out
