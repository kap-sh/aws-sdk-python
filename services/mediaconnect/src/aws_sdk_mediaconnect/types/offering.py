"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Offering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.duration_units
    import aws_sdk_mediaconnect.types.price_units
    import aws_sdk_mediaconnect.types.resource_specification


class Offering(TypedDict, closed=True):
    currency_code: NotRequired["str"]
    """<p> The type of currency that is used for billing. The currencyCode used for all reservations is US dollars.</p>"""
    duration: NotRequired["int"]
    """<p> The length of time that your reservation would be active.</p>"""
    duration_units: NotRequired[
        "aws_sdk_mediaconnect.types.duration_units.DurationUnits"
    ]
    """<p> The unit of measurement for the duration of the offering.</p>"""
    offering_arn: NotRequired["str"]
    """<p> The Amazon Resource Name (ARN) that MediaConnect assigns to the offering.</p>"""
    offering_description: NotRequired["str"]
    """<p> A description of the offering.</p>"""
    price_per_unit: NotRequired["str"]
    """<p> The cost of a single unit. This value, in combination with priceUnits, makes up the rate.</p>"""
    price_units: NotRequired["aws_sdk_mediaconnect.types.price_units.PriceUnits"]
    """<p> The unit of measurement that is used for billing. This value, in combination with pricePerUnit, makes up the rate.</p>"""
    resource_specification: NotRequired[
        "aws_sdk_mediaconnect.types.resource_specification.ResourceSpecification"
    ]
    """<p> A definition of the amount of outbound bandwidth that you would be reserving if you purchase the offering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Offering) -> dict:
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
    if "resource_specification" in value:
        import aws_sdk_mediaconnect.types.resource_specification

        out["resourceSpecification"] = (
            aws_sdk_mediaconnect.types.resource_specification.serialize_json(
                value["resource_specification"]
            )
        )
    return out


def deserialize_json(data: dict) -> Offering:
    out: Offering = {}  # type: ignore[typeddict-item]
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
    if "resourceSpecification" in data:
        import aws_sdk_mediaconnect.types.resource_specification

        out["resource_specification"] = (
            aws_sdk_mediaconnect.types.resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    return out
