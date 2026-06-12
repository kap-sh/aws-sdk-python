"""Generated from Smithy shape ``com.amazonaws.ivs#PlaybackRestrictionPolicyAllowedOriginList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.playback_restriction_policy_allowed_origin

PlaybackRestrictionPolicyAllowedOriginList: TypeAlias = list[
    "aws_sdk_ivs.types.playback_restriction_policy_allowed_origin.PlaybackRestrictionPolicyAllowedOrigin"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackRestrictionPolicyAllowedOriginList) -> list:
    return list(value)


def deserialize_json(data: list) -> PlaybackRestrictionPolicyAllowedOriginList:
    return list(data)
