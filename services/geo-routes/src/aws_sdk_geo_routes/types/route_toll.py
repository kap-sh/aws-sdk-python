"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteToll``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.country_code3
    import aws_sdk_geo_routes.types.index_list
    import aws_sdk_geo_routes.types.route_toll_payment_site_list
    import aws_sdk_geo_routes.types.route_toll_rate_list


class RouteToll(TypedDict, closed=True):
    country: NotRequired["aws_sdk_geo_routes.types.country_code3.CountryCode3"]
    """<p>The alpha-2 or alpha-3 character code for the country.</p>"""
    payment_sites: (
        "aws_sdk_geo_routes.types.route_toll_payment_site_list.RouteTollPaymentSiteList"
    )
    """<p>Locations or sites where the toll fare is collected.</p>"""
    rates: "aws_sdk_geo_routes.types.route_toll_rate_list.RouteTollRateList"
    """<p>Toll rates that need to be paid to travel this leg of the route.</p>"""
    systems: "aws_sdk_geo_routes.types.index_list.IndexList"
    """<p>Toll systems are authorities that collect payments for the toll.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteToll) -> dict:
    out: dict = {}
    if "country" in value:
        out["Country"] = value["country"]
    import aws_sdk_geo_routes.types.route_toll_payment_site_list

    out["PaymentSites"] = (
        aws_sdk_geo_routes.types.route_toll_payment_site_list.serialize_json(
            value["payment_sites"]
        )
    )
    import aws_sdk_geo_routes.types.route_toll_rate_list

    out["Rates"] = aws_sdk_geo_routes.types.route_toll_rate_list.serialize_json(
        value["rates"]
    )
    import aws_sdk_geo_routes.types.index_list

    out["Systems"] = aws_sdk_geo_routes.types.index_list.serialize_json(
        value["systems"]
    )
    return out


def deserialize_json(data: dict) -> RouteToll:
    out: RouteToll = {}  # type: ignore[typeddict-item]
    if "Country" in data:
        out["country"] = data["Country"]
    if "PaymentSites" in data:
        import aws_sdk_geo_routes.types.route_toll_payment_site_list

        out["payment_sites"] = (
            aws_sdk_geo_routes.types.route_toll_payment_site_list.deserialize_json(
                data["PaymentSites"]
            )
        )
    else:
        raise DeserializationError("RouteToll.payment_sites required")
    if "Rates" in data:
        import aws_sdk_geo_routes.types.route_toll_rate_list

        out["rates"] = aws_sdk_geo_routes.types.route_toll_rate_list.deserialize_json(
            data["Rates"]
        )
    else:
        raise DeserializationError("RouteToll.rates required")
    if "Systems" in data:
        import aws_sdk_geo_routes.types.index_list

        out["systems"] = aws_sdk_geo_routes.types.index_list.deserialize_json(
            data["Systems"]
        )
    else:
        raise DeserializationError("RouteToll.systems required")
    return out
