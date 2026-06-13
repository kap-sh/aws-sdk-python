"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Reservation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.duration_units
    import aws_sdk_mediaconnect.types.price_units
    import aws_sdk_mediaconnect.types.reservation_state
    import aws_sdk_mediaconnect.types.resource_specification


class Reservation(TypedDict):
    currency_code: NotRequired["str"]
    """<p> The type of currency that is used for billing. The currencyCode used for your reservation is US dollars.</p>"""
    duration: NotRequired["int"]
    """<p> The length of time that this reservation is active. MediaConnect defines this value in the offering.</p>"""
    duration_units: NotRequired[
        "aws_sdk_mediaconnect.types.duration_units.DurationUnits"
    ]
    """<p> The unit of measurement for the duration of the reservation. MediaConnect defines this value in the offering.</p>"""
    end: NotRequired["str"]
    """<p> The day and time that this reservation expires. This value is calculated based on the start date and time that you set and the offering's duration.</p>"""
    offering_arn: NotRequired["str"]
    """<p> The Amazon Resource Name (ARN) that MediaConnect assigns to the offering.</p>"""
    offering_description: NotRequired["str"]
    """<p> A description of the offering. MediaConnect defines this value in the offering.</p>"""
    price_per_unit: NotRequired["str"]
    """<p> The cost of a single unit. This value, in combination with priceUnits, makes up the rate. MediaConnect defines this value in the offering.</p>"""
    price_units: NotRequired["aws_sdk_mediaconnect.types.price_units.PriceUnits"]
    """<p> The unit of measurement that is used for billing. This value, in combination with pricePerUnit, makes up the rate. MediaConnect defines this value in the offering.</p>"""
    reservation_arn: NotRequired["str"]
    """<p> The Amazon Resource Name (ARN) that MediaConnect assigns to the reservation when you purchase an offering.</p>"""
    reservation_name: NotRequired["str"]
    """<p> The name that you assigned to the reservation when you purchased the offering.</p>"""
    reservation_state: NotRequired[
        "aws_sdk_mediaconnect.types.reservation_state.ReservationState"
    ]
    """<p> The status of your reservation.</p>"""
    resource_specification: NotRequired[
        "aws_sdk_mediaconnect.types.resource_specification.ResourceSpecification"
    ]
    """<p> A definition of the amount of outbound bandwidth that you would be reserving if you purchase the offering. MediaConnect defines the values that make up the resourceSpecification in the offering.</p>"""
    start: NotRequired["str"]
    """<p> The day and time that the reservation becomes active. You set this value when you purchase the offering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Reservation) -> dict:
    out: dict = {}
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "duration_units" in value:
        import aws_sdk_mediaconnect.types.duration_units

        out["durationUnits"] = aws_sdk_mediaconnect.types.duration_units.serialize_json(
            value["duration_units"]
        )
    if "end" in value:
        out["end"] = value["end"]
    if "offering_arn" in value:
        out["offeringArn"] = value["offering_arn"]
    if "offering_description" in value:
        out["offeringDescription"] = value["offering_description"]
    if "price_per_unit" in value:
        out["pricePerUnit"] = value["price_per_unit"]
    if "price_units" in value:
        import aws_sdk_mediaconnect.types.price_units

        out["priceUnits"] = aws_sdk_mediaconnect.types.price_units.serialize_json(
            value["price_units"]
        )
    if "reservation_arn" in value:
        out["reservationArn"] = value["reservation_arn"]
    if "reservation_name" in value:
        out["reservationName"] = value["reservation_name"]
    if "reservation_state" in value:
        import aws_sdk_mediaconnect.types.reservation_state

        out["reservationState"] = (
            aws_sdk_mediaconnect.types.reservation_state.serialize_json(
                value["reservation_state"]
            )
        )
    if "resource_specification" in value:
        import aws_sdk_mediaconnect.types.resource_specification

        out["resourceSpecification"] = (
            aws_sdk_mediaconnect.types.resource_specification.serialize_json(
                value["resource_specification"]
            )
        )
    if "start" in value:
        out["start"] = value["start"]
    return out


def deserialize_json(data: dict) -> Reservation:
    out: Reservation = {}  # type: ignore[typeddict-item]
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "durationUnits" in data:
        import aws_sdk_mediaconnect.types.duration_units

        out["duration_units"] = (
            aws_sdk_mediaconnect.types.duration_units.deserialize_json(
                data["durationUnits"]
            )
        )
    if "end" in data:
        out["end"] = data["end"]
    if "offeringArn" in data:
        out["offering_arn"] = data["offeringArn"]
    if "offeringDescription" in data:
        out["offering_description"] = data["offeringDescription"]
    if "pricePerUnit" in data:
        out["price_per_unit"] = data["pricePerUnit"]
    if "priceUnits" in data:
        import aws_sdk_mediaconnect.types.price_units

        out["price_units"] = aws_sdk_mediaconnect.types.price_units.deserialize_json(
            data["priceUnits"]
        )
    if "reservationArn" in data:
        out["reservation_arn"] = data["reservationArn"]
    if "reservationName" in data:
        out["reservation_name"] = data["reservationName"]
    if "reservationState" in data:
        import aws_sdk_mediaconnect.types.reservation_state

        out["reservation_state"] = (
            aws_sdk_mediaconnect.types.reservation_state.deserialize_json(
                data["reservationState"]
            )
        )
    if "resourceSpecification" in data:
        import aws_sdk_mediaconnect.types.resource_specification

        out["resource_specification"] = (
            aws_sdk_mediaconnect.types.resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    if "start" in data:
        out["start"] = data["start"]
    return out
