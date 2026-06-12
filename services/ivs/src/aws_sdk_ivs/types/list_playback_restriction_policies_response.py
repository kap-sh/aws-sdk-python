"""Generated from Smithy shape ``com.amazonaws.ivs#ListPlaybackRestrictionPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.pagination_token
    import aws_sdk_ivs.types.playback_restriction_policy_list


class ListPlaybackRestrictionPoliciesResponse(TypedDict):
    playback_restriction_policies: "aws_sdk_ivs.types.playback_restriction_policy_list.PlaybackRestrictionPolicyList"
    """<p>List of the matching policies.</p>"""
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more channels than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaybackRestrictionPoliciesResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.playback_restriction_policy_list

    out["playbackRestrictionPolicies"] = (
        aws_sdk_ivs.types.playback_restriction_policy_list.serialize_json(
            value["playback_restriction_policies"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPlaybackRestrictionPoliciesResponse:
    out: ListPlaybackRestrictionPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "playbackRestrictionPolicies" in data:
        import aws_sdk_ivs.types.playback_restriction_policy_list

        out["playback_restriction_policies"] = (
            aws_sdk_ivs.types.playback_restriction_policy_list.deserialize_json(
                data["playbackRestrictionPolicies"]
            )
        )
    else:
        raise DeserializationError(
            "ListPlaybackRestrictionPoliciesResponse.playback_restriction_policies required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
