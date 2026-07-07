"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.currency_code
    import aws_sdk_geo_routes.types.route_emission_type
    import aws_sdk_geo_routes.types.route_toll_vehicle_category
    import aws_sdk_geo_routes.types.sensitive_boolean


class RouteTollOptions(TypedDict, closed=True):
    all_transponders: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Specifies if the user has valid transponder with access to all toll systems. This impacts toll calculation, and if true the price with transponders is used.</p>"""
    all_vignettes: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Specifies if the user has valid vignettes with access for all toll roads. If a user has a vignette for a toll road, then toll cost for that road is omitted since no further payment is necessary.</p>"""
    currency: NotRequired["aws_sdk_geo_routes.types.currency_code.CurrencyCode"]
    """<p>Currency code corresponding to the price. This is the same as Currency specified in the request.</p>"""
    emission_type: NotRequired[
        "aws_sdk_geo_routes.types.route_emission_type.RouteEmissionType"
    ]
    """<p>Emission type of the vehicle for toll cost calculation.</p> <p> <b>Valid values</b>: <code>Euro1, Euro2, Euro3, Euro4, Euro5, Euro6, EuroEev</code> </p>"""
    vehicle_category: NotRequired[
        "aws_sdk_geo_routes.types.route_toll_vehicle_category.RouteTollVehicleCategory"
    ]
    """<p>Vehicle category for toll cost calculation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollOptions) -> dict:
    out: dict = {}
    if "all_transponders" in value:
        out["AllTransponders"] = value["all_transponders"]
    if "all_vignettes" in value:
        out["AllVignettes"] = value["all_vignettes"]
    if "currency" in value:
        out["Currency"] = value["currency"]
    if "emission_type" in value:
        import aws_sdk_geo_routes.types.route_emission_type

        out["EmissionType"] = (
            aws_sdk_geo_routes.types.route_emission_type.serialize_json(
                value["emission_type"]
            )
        )
    if "vehicle_category" in value:
        import aws_sdk_geo_routes.types.route_toll_vehicle_category

        out["VehicleCategory"] = (
            aws_sdk_geo_routes.types.route_toll_vehicle_category.serialize_json(
                value["vehicle_category"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTollOptions:
    out: RouteTollOptions = {}  # type: ignore[typeddict-item]
    if "AllTransponders" in data:
        out["all_transponders"] = data["AllTransponders"]
    if "AllVignettes" in data:
        out["all_vignettes"] = data["AllVignettes"]
    if "Currency" in data:
        out["currency"] = data["Currency"]
    if "EmissionType" in data:
        import aws_sdk_geo_routes.types.route_emission_type

        out["emission_type"] = (
            aws_sdk_geo_routes.types.route_emission_type.deserialize_json(
                data["EmissionType"]
            )
        )
    if "VehicleCategory" in data:
        import aws_sdk_geo_routes.types.route_toll_vehicle_category

        out["vehicle_category"] = (
            aws_sdk_geo_routes.types.route_toll_vehicle_category.deserialize_json(
                data["VehicleCategory"]
            )
        )
    return out
