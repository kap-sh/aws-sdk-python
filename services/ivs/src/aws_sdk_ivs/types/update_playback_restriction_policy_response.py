"""Generated from Smithy shape ``com.amazonaws.ivs#UpdatePlaybackRestrictionPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.playback_restriction_policy


class UpdatePlaybackRestrictionPolicyResponse(TypedDict, closed=True):
    playback_restriction_policy: NotRequired[
        "aws_sdk_ivs.types.playback_restriction_policy.PlaybackRestrictionPolicy"
    ]
    """<p>Object specifying the updated policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePlaybackRestrictionPolicyResponse) -> dict:
    out: dict = {}
    if "playback_restriction_policy" in value:
        import aws_sdk_ivs.types.playback_restriction_policy

        out["playbackRestrictionPolicy"] = (
            aws_sdk_ivs.types.playback_restriction_policy.serialize_json(
                value["playback_restriction_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePlaybackRestrictionPolicyResponse:
    out: UpdatePlaybackRestrictionPolicyResponse = {}  # type: ignore[typeddict-item]
    if "playbackRestrictionPolicy" in data:
        import aws_sdk_ivs.types.playback_restriction_policy

        out["playback_restriction_policy"] = (
            aws_sdk_ivs.types.playback_restriction_policy.deserialize_json(
                data["playbackRestrictionPolicy"]
            )
        )
    return out
