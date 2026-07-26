"""Generated from Smithy shape ``com.amazonaws.snowball#UpdateLongTermPricingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import capo_snowball.types.java_boolean
    import capo_snowball.types.job_id
    import capo_snowball.types.long_term_pricing_id


class UpdateLongTermPricingRequest(TypedDict, closed=True):
    long_term_pricing_id: "capo_snowball.types.long_term_pricing_id.LongTermPricingId"
    """<p>The ID of the long-term pricing type for the device.</p>"""
    replacement_job: NotRequired["capo_snowball.types.job_id.JobId"]
    """<p>Specifies that a device that is ordered with long-term pricing should be replaced with a new device.</p>"""
    is_long_term_pricing_auto_renew: NotRequired[
        "capo_snowball.types.java_boolean.JavaBoolean"
    ]
    """<p>If set to <code>true</code>, specifies that the current long-term pricing type for the device should be automatically renewed before the long-term pricing contract expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLongTermPricingRequest) -> dict:
    out: dict = {}
    out["LongTermPricingId"] = value["long_term_pricing_id"]
    if "replacement_job" in value:
        out["ReplacementJob"] = value["replacement_job"]
    if "is_long_term_pricing_auto_renew" in value:
        out["IsLongTermPricingAutoRenew"] = value["is_long_term_pricing_auto_renew"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLongTermPricingRequest:
    out: UpdateLongTermPricingRequest = {}  # type: ignore[typeddict-item]
    if "LongTermPricingId" in data:
        out["long_term_pricing_id"] = data["LongTermPricingId"]
    else:
        raise DeserializationError(
            "UpdateLongTermPricingRequest.long_term_pricing_id required"
        )
    if "ReplacementJob" in data:
        out["replacement_job"] = data["ReplacementJob"]
    if "IsLongTermPricingAutoRenew" in data:
        out["is_long_term_pricing_auto_renew"] = data["IsLongTermPricingAutoRenew"]
    return out
