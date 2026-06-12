"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalLegDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_attribution_list
    import aws_sdk_geo_routes.types.route_rental_after_travel_step_list
    import aws_sdk_geo_routes.types.route_rental_agency
    import aws_sdk_geo_routes.types.route_rental_arrival
    import aws_sdk_geo_routes.types.route_rental_before_travel_step_list
    import aws_sdk_geo_routes.types.route_rental_departure
    import aws_sdk_geo_routes.types.route_rental_summary
    import aws_sdk_geo_routes.types.route_rental_transport_mode_details
    import aws_sdk_geo_routes.types.route_rental_travel_step_list
    import aws_sdk_geo_routes.types.route_web_link_list


class RouteRentalLegDetails(TypedDict):
    after_travel_steps: "aws_sdk_geo_routes.types.route_rental_after_travel_step_list.RouteRentalAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    agency: "aws_sdk_geo_routes.types.route_rental_agency.RouteRentalAgency"
    """<p>Details about the rental agency.</p>"""
    arrival: "aws_sdk_geo_routes.types.route_rental_arrival.RouteRentalArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    attributions: "aws_sdk_geo_routes.types.route_attribution_list.RouteAttributionList"
    """<p>List of required attributions to display.</p>"""
    before_travel_steps: "aws_sdk_geo_routes.types.route_rental_before_travel_step_list.RouteRentalBeforeTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""
    booking_web_links: "aws_sdk_geo_routes.types.route_web_link_list.RouteWebLinkList"
    """<p>Web links to external ticket booking services for the rental.</p>"""
    departure: "aws_sdk_geo_routes.types.route_rental_departure.RouteRentalDeparture"
    """<p>Details corresponding to the departure for the leg.</p>"""
    summary: NotRequired[
        "aws_sdk_geo_routes.types.route_rental_summary.RouteRentalSummary"
    ]
    """<p>Summary of the rental leg.</p>"""
    transport: "aws_sdk_geo_routes.types.route_rental_transport_mode_details.RouteRentalTransportModeDetails"
    """<p>Transport mode details for the rental leg.</p>"""
    travel_steps: "aws_sdk_geo_routes.types.route_rental_travel_step_list.RouteRentalTravelStepList"
    """<p>Steps of a leg that must be performed during the travel portion of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalLegDetails) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_rental_after_travel_step_list

    out["AfterTravelSteps"] = (
        aws_sdk_geo_routes.types.route_rental_after_travel_step_list.serialize_json(
            value["after_travel_steps"]
        )
    )
    import aws_sdk_geo_routes.types.route_rental_agency

    out["Agency"] = aws_sdk_geo_routes.types.route_rental_agency.serialize_json(
        value["agency"]
    )
    import aws_sdk_geo_routes.types.route_rental_arrival

    out["Arrival"] = aws_sdk_geo_routes.types.route_rental_arrival.serialize_json(
        value["arrival"]
    )
    import aws_sdk_geo_routes.types.route_attribution_list

    out["Attributions"] = (
        aws_sdk_geo_routes.types.route_attribution_list.serialize_json(
            value["attributions"]
        )
    )
    import aws_sdk_geo_routes.types.route_rental_before_travel_step_list

    out["BeforeTravelSteps"] = (
        aws_sdk_geo_routes.types.route_rental_before_travel_step_list.serialize_json(
            value["before_travel_steps"]
        )
    )
    import aws_sdk_geo_routes.types.route_web_link_list

    out["BookingWebLinks"] = (
        aws_sdk_geo_routes.types.route_web_link_list.serialize_json(
            value["booking_web_links"]
        )
    )
    import aws_sdk_geo_routes.types.route_rental_departure

    out["Departure"] = aws_sdk_geo_routes.types.route_rental_departure.serialize_json(
        value["departure"]
    )
    if "summary" in value:
        import aws_sdk_geo_routes.types.route_rental_summary

        out["Summary"] = aws_sdk_geo_routes.types.route_rental_summary.serialize_json(
            value["summary"]
        )
    import aws_sdk_geo_routes.types.route_rental_transport_mode_details

    out["Transport"] = (
        aws_sdk_geo_routes.types.route_rental_transport_mode_details.serialize_json(
            value["transport"]
        )
    )
    import aws_sdk_geo_routes.types.route_rental_travel_step_list

    out["TravelSteps"] = (
        aws_sdk_geo_routes.types.route_rental_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteRentalLegDetails:
    out: RouteRentalLegDetails = {}  # type: ignore[typeddict-item]
    if "AfterTravelSteps" in data:
        import aws_sdk_geo_routes.types.route_rental_after_travel_step_list

        out["after_travel_steps"] = (
            aws_sdk_geo_routes.types.route_rental_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.after_travel_steps required")
    if "Agency" in data:
        import aws_sdk_geo_routes.types.route_rental_agency

        out["agency"] = aws_sdk_geo_routes.types.route_rental_agency.deserialize_json(
            data["Agency"]
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.agency required")
    if "Arrival" in data:
        import aws_sdk_geo_routes.types.route_rental_arrival

        out["arrival"] = aws_sdk_geo_routes.types.route_rental_arrival.deserialize_json(
            data["Arrival"]
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.arrival required")
    if "Attributions" in data:
        import aws_sdk_geo_routes.types.route_attribution_list

        out["attributions"] = (
            aws_sdk_geo_routes.types.route_attribution_list.deserialize_json(
                data["Attributions"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.attributions required")
    if "BeforeTravelSteps" in data:
        import aws_sdk_geo_routes.types.route_rental_before_travel_step_list

        out["before_travel_steps"] = (
            aws_sdk_geo_routes.types.route_rental_before_travel_step_list.deserialize_json(
                data["BeforeTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.before_travel_steps required")
    if "BookingWebLinks" in data:
        import aws_sdk_geo_routes.types.route_web_link_list

        out["booking_web_links"] = (
            aws_sdk_geo_routes.types.route_web_link_list.deserialize_json(
                data["BookingWebLinks"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.booking_web_links required")
    if "Departure" in data:
        import aws_sdk_geo_routes.types.route_rental_departure

        out["departure"] = (
            aws_sdk_geo_routes.types.route_rental_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.departure required")
    if "Summary" in data:
        import aws_sdk_geo_routes.types.route_rental_summary

        out["summary"] = aws_sdk_geo_routes.types.route_rental_summary.deserialize_json(
            data["Summary"]
        )
    if "Transport" in data:
        import aws_sdk_geo_routes.types.route_rental_transport_mode_details

        out["transport"] = (
            aws_sdk_geo_routes.types.route_rental_transport_mode_details.deserialize_json(
                data["Transport"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.transport required")
    if "TravelSteps" in data:
        import aws_sdk_geo_routes.types.route_rental_travel_step_list

        out["travel_steps"] = (
            aws_sdk_geo_routes.types.route_rental_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.travel_steps required")
    return out
