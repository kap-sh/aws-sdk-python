"""Generated from Smithy shape ``com.amazonaws.securityhub#GetEnabledStandardsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.next_token
    import capo_securityhub.types.standards_subscriptions


class GetEnabledStandardsResponse(TypedDict, closed=True):
    standards_subscriptions: NotRequired[
        "capo_securityhub.types.standards_subscriptions.StandardsSubscriptions"
    ]
    """<p>The list of <code>StandardsSubscriptions</code> objects that include information about the enabled standards.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnabledStandardsResponse) -> dict:
    out: dict = {}
    if "standards_subscriptions" in value:
        import capo_securityhub.types.standards_subscriptions

        out["StandardsSubscriptions"] = (
            capo_securityhub.types.standards_subscriptions.serialize_json(
                value["standards_subscriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEnabledStandardsResponse:
    out: GetEnabledStandardsResponse = {}  # type: ignore[typeddict-item]
    if "StandardsSubscriptions" in data:
        import capo_securityhub.types.standards_subscriptions

        out["standards_subscriptions"] = (
            capo_securityhub.types.standards_subscriptions.deserialize_json(
                data["StandardsSubscriptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
