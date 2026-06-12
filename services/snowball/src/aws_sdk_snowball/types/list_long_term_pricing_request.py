"""Generated from Smithy shape ``com.amazonaws.snowball#ListLongTermPricingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.list_limit
    import aws_sdk_snowball.types.string


class ListLongTermPricingRequest(TypedDict):
    max_results: NotRequired["aws_sdk_snowball.types.list_limit.ListLimit"]
    """<p>The maximum number of <code>ListLongTermPricing</code> objects to return.</p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>Because HTTP requests are stateless, this is the starting point for your next list of <code>ListLongTermPricing</code> to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLongTermPricingRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLongTermPricingRequest:
    out: ListLongTermPricingRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
