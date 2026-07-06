"""Generated from Smithy shape ``com.amazonaws.ivs#GetPlaybackRestrictionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.playback_restriction_policy_arn


class GetPlaybackRestrictionPolicyRequest(TypedDict, closed=True):
    arn: (
        "aws_sdk_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn"
    )
    """<p>ARN of the playback restriction policy to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaybackRestrictionPolicyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetPlaybackRestrictionPolicyRequest:
    out: GetPlaybackRestrictionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetPlaybackRestrictionPolicyRequest.arn required")
    return out
