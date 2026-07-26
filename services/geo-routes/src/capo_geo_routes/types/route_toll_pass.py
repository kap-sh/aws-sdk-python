"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPass``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_toll_pass_validity_period
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.sensitive_integer


class RouteTollPass(TypedDict, closed=True):
    includes_return_trip: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>If the pass includes the rate for the return leg of the trip.</p>"""
    senior_pass: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>If the pass is only valid for senior persons.</p>"""
    transfer_count: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>If the toll pass can be transferred, and how many times.</p>"""
    trip_count: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p>Number of trips the pass is valid for.</p>"""
    validity_period: NotRequired[
        "capo_geo_routes.types.route_toll_pass_validity_period.RouteTollPassValidityPeriod"
    ]
    """<p>Period for which the pass is valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPass) -> dict:
    out: dict = {}
    if "includes_return_trip" in value:
        out["IncludesReturnTrip"] = value["includes_return_trip"]
    if "senior_pass" in value:
        out["SeniorPass"] = value["senior_pass"]
    if "transfer_count" in value:
        out["TransferCount"] = value["transfer_count"]
    if "trip_count" in value:
        out["TripCount"] = value["trip_count"]
    if "validity_period" in value:
        import capo_geo_routes.types.route_toll_pass_validity_period

        out["ValidityPeriod"] = (
            capo_geo_routes.types.route_toll_pass_validity_period.serialize_json(
                value["validity_period"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTollPass:
    out: RouteTollPass = {}  # type: ignore[typeddict-item]
    if "IncludesReturnTrip" in data:
        out["includes_return_trip"] = data["IncludesReturnTrip"]
    if "SeniorPass" in data:
        out["senior_pass"] = data["SeniorPass"]
    if "TransferCount" in data:
        out["transfer_count"] = data["TransferCount"]
    if "TripCount" in data:
        out["trip_count"] = data["TripCount"]
    if "ValidityPeriod" in data:
        import capo_geo_routes.types.route_toll_pass_validity_period

        out["validity_period"] = (
            capo_geo_routes.types.route_toll_pass_validity_period.deserialize_json(
                data["ValidityPeriod"]
            )
        )
    return out
