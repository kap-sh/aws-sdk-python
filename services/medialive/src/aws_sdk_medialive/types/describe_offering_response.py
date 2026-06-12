"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeOfferingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.offering_duration_units
    import aws_sdk_medialive.types.offering_type
    import aws_sdk_medialive.types.reservation_resource_specification


class DescribeOfferingResponse(TypedDict):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Unique offering ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:offering:87654321'"""
    currency_code: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'"""
    duration: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """Lease duration, e.g. '12'"""
    duration_units: NotRequired[
        "aws_sdk_medialive.types.offering_duration_units.OfferingDurationUnits"
    ]
    """Units for duration, e.g. 'MONTHS'"""
    fixed_price: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT offering"""
    offering_description: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)'"""
    offering_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Unique offering ID, e.g. '87654321'"""
    offering_type: NotRequired["aws_sdk_medialive.types.offering_type.OfferingType"]
    """Offering type, e.g. 'NO_UPFRONT'"""
    region: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """AWS region, e.g. 'us-west-2'"""
    resource_specification: NotRequired[
        "aws_sdk_medialive.types.reservation_resource_specification.ReservationResourceSpecification"
    ]
    """Resource configuration details"""
    usage_price: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Recurring usage charge for each reserved resource, e.g. '157.0'"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOfferingResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
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
    if "fixed_price" in value:
        out["fixedPrice"] = value["fixed_price"]
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
    if "resource_specification" in value:
        import aws_sdk_medialive.types.reservation_resource_specification

        out["resourceSpecification"] = (
            aws_sdk_medialive.types.reservation_resource_specification.serialize_json(
                value["resource_specification"]
            )
        )
    if "usage_price" in value:
        out["usagePrice"] = value["usage_price"]
    return out


def deserialize_json(data: dict) -> DescribeOfferingResponse:
    out: DescribeOfferingResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
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
    if "fixedPrice" in data:
        out["fixed_price"] = data["fixedPrice"]
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
    if "resourceSpecification" in data:
        import aws_sdk_medialive.types.reservation_resource_specification

        out["resource_specification"] = (
            aws_sdk_medialive.types.reservation_resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    if "usagePrice" in data:
        out["usage_price"] = data["usagePrice"]
    return out
