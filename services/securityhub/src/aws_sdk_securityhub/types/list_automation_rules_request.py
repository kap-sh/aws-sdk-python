"""Generated from Smithy shape ``com.amazonaws.securityhub#ListAutomationRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token


class ListAutomationRulesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p> A token to specify where to start paginating the response. This is the <code>NextToken</code> from a previously truncated response. On your first call to the <code>ListAutomationRules</code> API, set the value of this parameter to <code>NULL</code>. </p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p> The maximum number of rules to return in the response. This currently ranges from 1 to 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomationRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAutomationRulesRequest:
    out: ListAutomationRulesRequest = {}  # type: ignore[typeddict-item]
    return out
