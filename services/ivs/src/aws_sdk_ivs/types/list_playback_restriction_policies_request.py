"""Generated from Smithy shape ``com.amazonaws.ivs#ListPlaybackRestrictionPoliciesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.max_playback_restriction_policy_results
    import aws_sdk_ivs.types.pagination_token


class ListPlaybackRestrictionPoliciesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>The first policy to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "aws_sdk_ivs.types.max_playback_restriction_policy_results.MaxPlaybackRestrictionPolicyResults"
    ]
    """<p>Maximum number of policies to return. Default: 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaybackRestrictionPoliciesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListPlaybackRestrictionPoliciesRequest:
    out: ListPlaybackRestrictionPoliciesRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
