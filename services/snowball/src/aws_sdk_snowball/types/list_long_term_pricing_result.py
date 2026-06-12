"""Generated from Smithy shape ``com.amazonaws.snowball#ListLongTermPricingResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.long_term_pricing_entry_list
    import aws_sdk_snowball.types.string


class ListLongTermPricingResult(TypedDict):
    long_term_pricing_entries: NotRequired[
        "aws_sdk_snowball.types.long_term_pricing_entry_list.LongTermPricingEntryList"
    ]
    """<p>Each <code>LongTermPricingEntry</code> object contains a status, ID, and other information about the <code>LongTermPricing</code> type. </p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>Because HTTP requests are stateless, this is the starting point for your next list of returned <code>ListLongTermPricing</code> list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLongTermPricingResult) -> dict:
    out: dict = {}
    if "long_term_pricing_entries" in value:
        import aws_sdk_snowball.types.long_term_pricing_entry_list

        out["LongTermPricingEntries"] = (
            aws_sdk_snowball.types.long_term_pricing_entry_list.serialize_aws_json_1_1(
                value["long_term_pricing_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLongTermPricingResult:
    out: ListLongTermPricingResult = {}  # type: ignore[typeddict-item]
    if "LongTermPricingEntries" in data:
        import aws_sdk_snowball.types.long_term_pricing_entry_list

        out["long_term_pricing_entries"] = (
            aws_sdk_snowball.types.long_term_pricing_entry_list.deserialize_aws_json_1_1(
                data["LongTermPricingEntries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
