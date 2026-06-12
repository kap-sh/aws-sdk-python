"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiLegDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_attribution_list
    import aws_sdk_geo_routes.types.route_taxi_after_travel_step_list
    import aws_sdk_geo_routes.types.route_taxi_agency
    import aws_sdk_geo_routes.types.route_taxi_arrival
    import aws_sdk_geo_routes.types.route_taxi_before_travel_step_list
    import aws_sdk_geo_routes.types.route_taxi_departure
    import aws_sdk_geo_routes.types.route_taxi_notice_list
    import aws_sdk_geo_routes.types.route_taxi_summary
    import aws_sdk_geo_routes.types.route_taxi_transport_mode_details
    import aws_sdk_geo_routes.types.route_taxi_travel_step_list
    import aws_sdk_geo_routes.types.route_web_link_list


class RouteTaxiLegDetails(TypedDict):
    after_travel_steps: "aws_sdk_geo_routes.types.route_taxi_after_travel_step_list.RouteTaxiAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    agency: "aws_sdk_geo_routes.types.route_taxi_agency.RouteTaxiAgency"
    """<p>Details about the taxi agency.</p>"""
    arrival: "aws_sdk_geo_routes.types.route_taxi_arrival.RouteTaxiArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    attributions: "aws_sdk_geo_routes.types.route_attribution_list.RouteAttributionList"
    """<p>List of required attributions to display.</p>"""
    before_travel_steps: "aws_sdk_geo_routes.types.route_taxi_before_travel_step_list.RouteTaxiBeforeTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""
    booking_web_links: "aws_sdk_geo_routes.types.route_web_link_list.RouteWebLinkList"
    """<p>Web links to external ticket booking services for the taxi.</p>"""
    departure: "aws_sdk_geo_routes.types.route_taxi_departure.RouteTaxiDeparture"
    """<p>Details corresponding to the departure for the leg.</p>"""
    notices: "aws_sdk_geo_routes.types.route_taxi_notice_list.RouteTaxiNoticeList"
    """<p>List of notices that indicate issues that occurred during route calculation.</p>"""
    summary: NotRequired["aws_sdk_geo_routes.types.route_taxi_summary.RouteTaxiSummary"]
    """<p>Summary of the taxi leg.</p>"""
    transport: "aws_sdk_geo_routes.types.route_taxi_transport_mode_details.RouteTaxiTransportModeDetails"
    """<p>Transport mode details for the taxi leg.</p>"""
    travel_steps: (
        "aws_sdk_geo_routes.types.route_taxi_travel_step_list.RouteTaxiTravelStepList"
    )
    """<p>Steps of a leg that must be performed during the travel portion of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiLegDetails) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_taxi_after_travel_step_list

    out["AfterTravelSteps"] = (
        aws_sdk_geo_routes.types.route_taxi_after_travel_step_list.serialize_json(
            value["after_travel_steps"]
        )
    )
    import aws_sdk_geo_routes.types.route_taxi_agency

    out["Agency"] = aws_sdk_geo_routes.types.route_taxi_agency.serialize_json(
        value["agency"]
    )
    import aws_sdk_geo_routes.types.route_taxi_arrival

    out["Arrival"] = aws_sdk_geo_routes.types.route_taxi_arrival.serialize_json(
        value["arrival"]
    )
    import aws_sdk_geo_routes.types.route_attribution_list

    out["Attributions"] = (
        aws_sdk_geo_routes.types.route_attribution_list.serialize_json(
            value["attributions"]
        )
    )
    import aws_sdk_geo_routes.types.route_taxi_before_travel_step_list

    out["BeforeTravelSteps"] = (
        aws_sdk_geo_routes.types.route_taxi_before_travel_step_list.serialize_json(
            value["before_travel_steps"]
        )
    )
    import aws_sdk_geo_routes.types.route_web_link_list

    out["BookingWebLinks"] = (
        aws_sdk_geo_routes.types.route_web_link_list.serialize_json(
            value["booking_web_links"]
        )
    )
    import aws_sdk_geo_routes.types.route_taxi_departure

    out["Departure"] = aws_sdk_geo_routes.types.route_taxi_departure.serialize_json(
        value["departure"]
    )
    import aws_sdk_geo_routes.types.route_taxi_notice_list

    out["Notices"] = aws_sdk_geo_routes.types.route_taxi_notice_list.serialize_json(
        value["notices"]
    )
    if "summary" in value:
        import aws_sdk_geo_routes.types.route_taxi_summary

        out["Summary"] = aws_sdk_geo_routes.types.route_taxi_summary.serialize_json(
            value["summary"]
        )
    import aws_sdk_geo_routes.types.route_taxi_transport_mode_details

    out["Transport"] = (
        aws_sdk_geo_routes.types.route_taxi_transport_mode_details.serialize_json(
            value["transport"]
        )
    )
    import aws_sdk_geo_routes.types.route_taxi_travel_step_list

    out["TravelSteps"] = (
        aws_sdk_geo_routes.types.route_taxi_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteTaxiLegDetails:
    out: RouteTaxiLegDetails = {}  # type: ignore[typeddict-item]
    if "AfterTravelSteps" in data:
        import aws_sdk_geo_routes.types.route_taxi_after_travel_step_list

        out["after_travel_steps"] = (
            aws_sdk_geo_routes.types.route_taxi_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.after_travel_steps required")
    if "Agency" in data:
        import aws_sdk_geo_routes.types.route_taxi_agency

        out["agency"] = aws_sdk_geo_routes.types.route_taxi_agency.deserialize_json(
            data["Agency"]
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.agency required")
    if "Arrival" in data:
        import aws_sdk_geo_routes.types.route_taxi_arrival

        out["arrival"] = aws_sdk_geo_routes.types.route_taxi_arrival.deserialize_json(
            data["Arrival"]
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.arrival required")
    if "Attributions" in data:
        import aws_sdk_geo_routes.types.route_attribution_list

        out["attributions"] = (
            aws_sdk_geo_routes.types.route_attribution_list.deserialize_json(
                data["Attributions"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.attributions required")
    if "BeforeTravelSteps" in data:
        import aws_sdk_geo_routes.types.route_taxi_before_travel_step_list

        out["before_travel_steps"] = (
            aws_sdk_geo_routes.types.route_taxi_before_travel_step_list.deserialize_json(
                data["BeforeTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.before_travel_steps required")
    if "BookingWebLinks" in data:
        import aws_sdk_geo_routes.types.route_web_link_list

        out["booking_web_links"] = (
            aws_sdk_geo_routes.types.route_web_link_list.deserialize_json(
                data["BookingWebLinks"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.booking_web_links required")
    if "Departure" in data:
        import aws_sdk_geo_routes.types.route_taxi_departure

        out["departure"] = (
            aws_sdk_geo_routes.types.route_taxi_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.departure required")
    if "Notices" in data:
        import aws_sdk_geo_routes.types.route_taxi_notice_list

        out["notices"] = (
            aws_sdk_geo_routes.types.route_taxi_notice_list.deserialize_json(
                data["Notices"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.notices required")
    if "Summary" in data:
        import aws_sdk_geo_routes.types.route_taxi_summary

        out["summary"] = aws_sdk_geo_routes.types.route_taxi_summary.deserialize_json(
            data["Summary"]
        )
    if "Transport" in data:
        import aws_sdk_geo_routes.types.route_taxi_transport_mode_details

        out["transport"] = (
            aws_sdk_geo_routes.types.route_taxi_transport_mode_details.deserialize_json(
                data["Transport"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.transport required")
    if "TravelSteps" in data:
        import aws_sdk_geo_routes.types.route_taxi_travel_step_list

        out["travel_steps"] = (
            aws_sdk_geo_routes.types.route_taxi_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.travel_steps required")
    return out
