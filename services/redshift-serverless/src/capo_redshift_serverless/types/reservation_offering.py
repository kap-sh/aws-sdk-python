"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ReservationOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.charge
    import capo_redshift_serverless.types.currency_code
    import capo_redshift_serverless.types.duration
    import capo_redshift_serverless.types.offering_id
    import capo_redshift_serverless.types.offering_type


class ReservationOffering(TypedDict, closed=True):
    offering_id: NotRequired["capo_redshift_serverless.types.offering_id.OfferingId"]
    """<p>The offering identifier.</p>"""
    duration: "capo_redshift_serverless.types.duration.Duration"
    """<p>The duration, in seconds, for which the reservation reserves the RPUs.</p>"""
    upfront_charge: "capo_redshift_serverless.types.charge.Charge"
    """<p>The up-front price you are charged for the reservation.</p>"""
    hourly_charge: "capo_redshift_serverless.types.charge.Charge"
    """<p>The rate you are charged for each hour the reservation is active.</p>"""
    currency_code: NotRequired[
        "capo_redshift_serverless.types.currency_code.CurrencyCode"
    ]
    """<p>The currency code for the offering.</p>"""
    offering_type: NotRequired[
        "capo_redshift_serverless.types.offering_type.OfferingType"
    ]
    """<p>Determines the payment schedule for the reservation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationOffering) -> dict:
    out: dict = {}
    if "offering_id" in value:
        out["offeringId"] = value["offering_id"]
    out["duration"] = value.get("duration", 0)
    out["upfrontCharge"] = value.get("upfront_charge", 0)
    out["hourlyCharge"] = value.get("hourly_charge", 0)
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "offering_type" in value:
        out["offeringType"] = value["offering_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservationOffering:
    out: ReservationOffering = {}  # type: ignore[typeddict-item]
    if "offeringId" in data:
        out["offering_id"] = data["offeringId"]
    if "duration" in data:
        out["duration"] = data["duration"]
    else:
        out["duration"] = 0
    if "upfrontCharge" in data:
        out["upfront_charge"] = data["upfrontCharge"]
    else:
        out["upfront_charge"] = 0
    if "hourlyCharge" in data:
        out["hourly_charge"] = data["hourlyCharge"]
    else:
        out["hourly_charge"] = 0
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    if "offeringType" in data:
        out["offering_type"] = data["offeringType"]
    return out
