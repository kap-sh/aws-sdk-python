"""Generated from Smithy shape ``com.amazonaws.ivs#CreatePlaybackRestrictionPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.playback_restriction_policy


class CreatePlaybackRestrictionPolicyResponse(TypedDict, closed=True):
    playback_restriction_policy: NotRequired[
        "aws_sdk_ivs.types.playback_restriction_policy.PlaybackRestrictionPolicy"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePlaybackRestrictionPolicyResponse) -> dict:
    out: dict = {}
    if "playback_restriction_policy" in value:
        import aws_sdk_ivs.types.playback_restriction_policy

        out["playbackRestrictionPolicy"] = (
            aws_sdk_ivs.types.playback_restriction_policy.serialize_json(
                value["playback_restriction_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreatePlaybackRestrictionPolicyResponse:
    out: CreatePlaybackRestrictionPolicyResponse = {}  # type: ignore[typeddict-item]
    if "playbackRestrictionPolicy" in data:
        import aws_sdk_ivs.types.playback_restriction_policy

        out["playback_restriction_policy"] = (
            aws_sdk_ivs.types.playback_restriction_policy.deserialize_json(
                data["playbackRestrictionPolicy"]
            )
        )
    return out
