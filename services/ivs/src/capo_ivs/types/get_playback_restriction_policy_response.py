"""Generated from Smithy shape ``com.amazonaws.ivs#GetPlaybackRestrictionPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.playback_restriction_policy


class GetPlaybackRestrictionPolicyResponse(TypedDict, closed=True):
    playback_restriction_policy: NotRequired[
        "capo_ivs.types.playback_restriction_policy.PlaybackRestrictionPolicy"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaybackRestrictionPolicyResponse) -> dict:
    out: dict = {}
    if "playback_restriction_policy" in value:
        import capo_ivs.types.playback_restriction_policy

        out["playbackRestrictionPolicy"] = (
            capo_ivs.types.playback_restriction_policy.serialize_json(
                value["playback_restriction_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPlaybackRestrictionPolicyResponse:
    out: GetPlaybackRestrictionPolicyResponse = {}  # type: ignore[typeddict-item]
    if "playbackRestrictionPolicy" in data:
        import capo_ivs.types.playback_restriction_policy

        out["playback_restriction_policy"] = (
            capo_ivs.types.playback_restriction_policy.deserialize_json(
                data["playbackRestrictionPolicy"]
            )
        )
    return out
