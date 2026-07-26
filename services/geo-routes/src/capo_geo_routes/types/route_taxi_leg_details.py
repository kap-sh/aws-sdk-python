"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiLegDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_attribution_list
    import capo_geo_routes.types.route_taxi_after_travel_step_list
    import capo_geo_routes.types.route_taxi_agency
    import capo_geo_routes.types.route_taxi_arrival
    import capo_geo_routes.types.route_taxi_before_travel_step_list
    import capo_geo_routes.types.route_taxi_departure
    import capo_geo_routes.types.route_taxi_notice_list
    import capo_geo_routes.types.route_taxi_summary
    import capo_geo_routes.types.route_taxi_transport_mode_details
    import capo_geo_routes.types.route_taxi_travel_step_list
    import capo_geo_routes.types.route_web_link_list


class RouteTaxiLegDetails(TypedDict, closed=True):
    after_travel_steps: "capo_geo_routes.types.route_taxi_after_travel_step_list.RouteTaxiAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    agency: "capo_geo_routes.types.route_taxi_agency.RouteTaxiAgency"
    """<p>Details about the taxi agency.</p>"""
    arrival: "capo_geo_routes.types.route_taxi_arrival.RouteTaxiArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    attributions: "capo_geo_routes.types.route_attribution_list.RouteAttributionList"
    """<p>List of required attributions to display.</p>"""
    before_travel_steps: "capo_geo_routes.types.route_taxi_before_travel_step_list.RouteTaxiBeforeTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""
    booking_web_links: "capo_geo_routes.types.route_web_link_list.RouteWebLinkList"
    """<p>Web links to external ticket booking services for the taxi.</p>"""
    departure: "capo_geo_routes.types.route_taxi_departure.RouteTaxiDeparture"
    """<p>Details corresponding to the departure for the leg.</p>"""
    notices: "capo_geo_routes.types.route_taxi_notice_list.RouteTaxiNoticeList"
    """<p>List of notices that indicate issues that occurred during route calculation.</p>"""
    summary: NotRequired["capo_geo_routes.types.route_taxi_summary.RouteTaxiSummary"]
    """<p>Summary of the taxi leg.</p>"""
    transport: "capo_geo_routes.types.route_taxi_transport_mode_details.RouteTaxiTransportModeDetails"
    """<p>Transport mode details for the taxi leg.</p>"""
    travel_steps: (
        "capo_geo_routes.types.route_taxi_travel_step_list.RouteTaxiTravelStepList"
    )
    """<p>Steps of a leg that must be performed during the travel portion of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiLegDetails) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_taxi_after_travel_step_list

    out["AfterTravelSteps"] = (
        capo_geo_routes.types.route_taxi_after_travel_step_list.serialize_json(
            value["after_travel_steps"]
        )
    )
    import capo_geo_routes.types.route_taxi_agency

    out["Agency"] = capo_geo_routes.types.route_taxi_agency.serialize_json(
        value["agency"]
    )
    import capo_geo_routes.types.route_taxi_arrival

    out["Arrival"] = capo_geo_routes.types.route_taxi_arrival.serialize_json(
        value["arrival"]
    )
    import capo_geo_routes.types.route_attribution_list

    out["Attributions"] = capo_geo_routes.types.route_attribution_list.serialize_json(
        value["attributions"]
    )
    import capo_geo_routes.types.route_taxi_before_travel_step_list

    out["BeforeTravelSteps"] = (
        capo_geo_routes.types.route_taxi_before_travel_step_list.serialize_json(
            value["before_travel_steps"]
        )
    )
    import capo_geo_routes.types.route_web_link_list

    out["BookingWebLinks"] = capo_geo_routes.types.route_web_link_list.serialize_json(
        value["booking_web_links"]
    )
    import capo_geo_routes.types.route_taxi_departure

    out["Departure"] = capo_geo_routes.types.route_taxi_departure.serialize_json(
        value["departure"]
    )
    import capo_geo_routes.types.route_taxi_notice_list

    out["Notices"] = capo_geo_routes.types.route_taxi_notice_list.serialize_json(
        value["notices"]
    )
    if "summary" in value:
        import capo_geo_routes.types.route_taxi_summary

        out["Summary"] = capo_geo_routes.types.route_taxi_summary.serialize_json(
            value["summary"]
        )
    import capo_geo_routes.types.route_taxi_transport_mode_details

    out["Transport"] = (
        capo_geo_routes.types.route_taxi_transport_mode_details.serialize_json(
            value["transport"]
        )
    )
    import capo_geo_routes.types.route_taxi_travel_step_list

    out["TravelSteps"] = (
        capo_geo_routes.types.route_taxi_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteTaxiLegDetails:
    out: RouteTaxiLegDetails = {}  # type: ignore[typeddict-item]
    if "AfterTravelSteps" in data:
        import capo_geo_routes.types.route_taxi_after_travel_step_list

        out["after_travel_steps"] = (
            capo_geo_routes.types.route_taxi_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.after_travel_steps required")
    if "Agency" in data:
        import capo_geo_routes.types.route_taxi_agency

        out["agency"] = capo_geo_routes.types.route_taxi_agency.deserialize_json(
            data["Agency"]
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.agency required")
    if "Arrival" in data:
        import capo_geo_routes.types.route_taxi_arrival

        out["arrival"] = capo_geo_routes.types.route_taxi_arrival.deserialize_json(
            data["Arrival"]
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.arrival required")
    if "Attributions" in data:
        import capo_geo_routes.types.route_attribution_list

        out["attributions"] = (
            capo_geo_routes.types.route_attribution_list.deserialize_json(
                data["Attributions"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.attributions required")
    if "BeforeTravelSteps" in data:
        import capo_geo_routes.types.route_taxi_before_travel_step_list

        out["before_travel_steps"] = (
            capo_geo_routes.types.route_taxi_before_travel_step_list.deserialize_json(
                data["BeforeTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.before_travel_steps required")
    if "BookingWebLinks" in data:
        import capo_geo_routes.types.route_web_link_list

        out["booking_web_links"] = (
            capo_geo_routes.types.route_web_link_list.deserialize_json(
                data["BookingWebLinks"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.booking_web_links required")
    if "Departure" in data:
        import capo_geo_routes.types.route_taxi_departure

        out["departure"] = capo_geo_routes.types.route_taxi_departure.deserialize_json(
            data["Departure"]
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.departure required")
    if "Notices" in data:
        import capo_geo_routes.types.route_taxi_notice_list

        out["notices"] = capo_geo_routes.types.route_taxi_notice_list.deserialize_json(
            data["Notices"]
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.notices required")
    if "Summary" in data:
        import capo_geo_routes.types.route_taxi_summary

        out["summary"] = capo_geo_routes.types.route_taxi_summary.deserialize_json(
            data["Summary"]
        )
    if "Transport" in data:
        import capo_geo_routes.types.route_taxi_transport_mode_details

        out["transport"] = (
            capo_geo_routes.types.route_taxi_transport_mode_details.deserialize_json(
                data["Transport"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.transport required")
    if "TravelSteps" in data:
        import capo_geo_routes.types.route_taxi_travel_step_list

        out["travel_steps"] = (
            capo_geo_routes.types.route_taxi_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiLegDetails.travel_steps required")
    return out
