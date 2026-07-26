"""Generated from Smithy shape ``com.amazonaws.snowball#CreateLongTermPricingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.long_term_pricing_id


class CreateLongTermPricingResult(TypedDict, closed=True):
    long_term_pricing_id: NotRequired[
        "capo_snowball.types.long_term_pricing_id.LongTermPricingId"
    ]
    """<p>The ID of the long-term pricing type for the device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLongTermPricingResult) -> dict:
    out: dict = {}
    if "long_term_pricing_id" in value:
        out["LongTermPricingId"] = value["long_term_pricing_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLongTermPricingResult:
    out: CreateLongTermPricingResult = {}  # type: ignore[typeddict-item]
    if "LongTermPricingId" in data:
        out["long_term_pricing_id"] = data["LongTermPricingId"]
    return out
