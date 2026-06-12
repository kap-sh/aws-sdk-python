"""Generated from Smithy shape ``com.amazonaws.ivs#DeletePlaybackRestrictionPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.playback_restriction_policy_arn


class DeletePlaybackRestrictionPolicyRequest(TypedDict):
    arn: (
        "aws_sdk_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn"
    )
    """<p>ARN of the playback restriction policy to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePlaybackRestrictionPolicyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeletePlaybackRestrictionPolicyRequest:
    out: DeletePlaybackRestrictionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "DeletePlaybackRestrictionPolicyRequest.arn required"
        )
    return out
