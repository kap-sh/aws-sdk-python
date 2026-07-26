"""Generated from Smithy shape ``com.amazonaws.securityhub#ListAutomationRulesV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token


class ListAutomationRulesV2Request(TypedDict, closed=True):
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomationRulesV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAutomationRulesV2Request:
    out: ListAutomationRulesV2Request = {}  # type: ignore[typeddict-item]
    return out
