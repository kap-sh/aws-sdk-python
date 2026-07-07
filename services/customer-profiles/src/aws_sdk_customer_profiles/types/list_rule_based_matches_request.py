"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRuleBasedMatchesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.token


class ListRuleBasedMatchesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous <code>ListRuleBasedMatches</code> API call.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of <code>MatchIds</code> returned per page.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuleBasedMatchesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRuleBasedMatchesRequest:
    out: ListRuleBasedMatchesRequest = {}  # type: ignore[typeddict-item]
    return out
