"""Generated from Smithy shape ``com.amazonaws.ivs#PlaybackRestrictionPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.playback_restriction_policy_summary

PlaybackRestrictionPolicyList: TypeAlias = list[
    "capo_ivs.types.playback_restriction_policy_summary.PlaybackRestrictionPolicySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackRestrictionPolicyList) -> list:
    import capo_ivs.types.playback_restriction_policy_summary

    out: list = []
    for item in value:
        out.append(
            capo_ivs.types.playback_restriction_policy_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PlaybackRestrictionPolicyList:
    import capo_ivs.types.playback_restriction_policy_summary

    out: PlaybackRestrictionPolicyList = []
    for item in data:
        out.append(
            capo_ivs.types.playback_restriction_policy_summary.deserialize_json(item)
        )
    return out
