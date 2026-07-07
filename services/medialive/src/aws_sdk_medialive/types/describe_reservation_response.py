"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeReservationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.offering_duration_units
    import aws_sdk_medialive.types.offering_type
    import aws_sdk_medialive.types.renewal_settings
    import aws_sdk_medialive.types.reservation_resource_specification
    import aws_sdk_medialive.types.reservation_state
    import aws_sdk_medialive.types.tags


class DescribeReservationResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Unique reservation ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:reservation:1234567'"""
    count: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """Number of reserved resources"""
    currency_code: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'"""
    duration: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """Lease duration, e.g. '12'"""
    duration_units: NotRequired[
        "aws_sdk_medialive.types.offering_duration_units.OfferingDurationUnits"
    ]
    """Units for duration, e.g. 'MONTHS'"""
    end: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Reservation UTC end date and time in ISO-8601 format, e.g. '2019-03-01T00:00:00'"""
    fixed_price: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT offering"""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """User specified reservation name"""
    offering_description: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)'"""
    offering_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Unique offering ID, e.g. '87654321'"""
    offering_type: NotRequired["aws_sdk_medialive.types.offering_type.OfferingType"]
    """Offering type, e.g. 'NO_UPFRONT'"""
    region: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """AWS region, e.g. 'us-west-2'"""
    renewal_settings: NotRequired[
        "aws_sdk_medialive.types.renewal_settings.RenewalSettings"
    ]
    """Renewal settings for the reservation"""
    reservation_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Unique reservation ID, e.g. '1234567'"""
    resource_specification: NotRequired[
        "aws_sdk_medialive.types.reservation_resource_specification.ReservationResourceSpecification"
    ]
    """Resource configuration details"""
    start: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Reservation UTC start date and time in ISO-8601 format, e.g. '2018-03-01T00:00:00'"""
    state: NotRequired["aws_sdk_medialive.types.reservation_state.ReservationState"]
    """Current state of reservation, e.g. 'ACTIVE'"""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs"""
    usage_price: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Recurring usage charge for each reserved resource, e.g. '157.0'"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "count" in value:
        out["count"] = value["count"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "duration_units" in value:
        import aws_sdk_medialive.types.offering_duration_units

        out["durationUnits"] = (
            aws_sdk_medialive.types.offering_duration_units.serialize_json(
                value["duration_units"]
            )
        )
    if "end" in value:
        out["end"] = value["end"]
    if "fixed_price" in value:
        out["fixedPrice"] = value["fixed_price"]
    if "name" in value:
        out["name"] = value["name"]
    if "offering_description" in value:
        out["offeringDescription"] = value["offering_description"]
    if "offering_id" in value:
        out["offeringId"] = value["offering_id"]
    if "offering_type" in value:
        import aws_sdk_medialive.types.offering_type

        out["offeringType"] = aws_sdk_medialive.types.offering_type.serialize_json(
            value["offering_type"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "renewal_settings" in value:
        import aws_sdk_medialive.types.renewal_settings

        out["renewalSettings"] = (
            aws_sdk_medialive.types.renewal_settings.serialize_json(
                value["renewal_settings"]
            )
        )
    if "reservation_id" in value:
        out["reservationId"] = value["reservation_id"]
    if "resource_specification" in value:
        import aws_sdk_medialive.types.reservation_resource_specification

        out["resourceSpecification"] = (
            aws_sdk_medialive.types.reservation_resource_specification.serialize_json(
                value["resource_specification"]
            )
        )
    if "start" in value:
        out["start"] = value["start"]
    if "state" in value:
        import aws_sdk_medialive.types.reservation_state

        out["state"] = aws_sdk_medialive.types.reservation_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    if "usage_price" in value:
        out["usagePrice"] = value["usage_price"]
    return out


def deserialize_json(data: dict) -> DescribeReservationResponse:
    out: DescribeReservationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "count" in data:
        out["count"] = data["count"]
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "durationUnits" in data:
        import aws_sdk_medialive.types.offering_duration_units

        out["duration_units"] = (
            aws_sdk_medialive.types.offering_duration_units.deserialize_json(
                data["durationUnits"]
            )
        )
    if "end" in data:
        out["end"] = data["end"]
    if "fixedPrice" in data:
        out["fixed_price"] = data["fixedPrice"]
    if "name" in data:
        out["name"] = data["name"]
    if "offeringDescription" in data:
        out["offering_description"] = data["offeringDescription"]
    if "offeringId" in data:
        out["offering_id"] = data["offeringId"]
    if "offeringType" in data:
        import aws_sdk_medialive.types.offering_type

        out["offering_type"] = aws_sdk_medialive.types.offering_type.deserialize_json(
            data["offeringType"]
        )
    if "region" in data:
        out["region"] = data["region"]
    if "renewalSettings" in data:
        import aws_sdk_medialive.types.renewal_settings

        out["renewal_settings"] = (
            aws_sdk_medialive.types.renewal_settings.deserialize_json(
                data["renewalSettings"]
            )
        )
    if "reservationId" in data:
        out["reservation_id"] = data["reservationId"]
    if "resourceSpecification" in data:
        import aws_sdk_medialive.types.reservation_resource_specification

        out["resource_specification"] = (
            aws_sdk_medialive.types.reservation_resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    if "start" in data:
        out["start"] = data["start"]
    if "state" in data:
        import aws_sdk_medialive.types.reservation_state

        out["state"] = aws_sdk_medialive.types.reservation_state.deserialize_json(
            data["state"]
        )
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    if "usagePrice" in data:
        out["usage_price"] = data["usagePrice"]
    return out
