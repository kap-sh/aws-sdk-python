"""Generated from Smithy shape ``com.amazonaws.ivs#PlaybackRestrictionPolicyAllowedCountryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.playback_restriction_policy_allowed_country

PlaybackRestrictionPolicyAllowedCountryList: TypeAlias = list[
    "capo_ivs.types.playback_restriction_policy_allowed_country.PlaybackRestrictionPolicyAllowedCountry"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackRestrictionPolicyAllowedCountryList) -> list:
    return list(value)


def deserialize_json(data: list) -> PlaybackRestrictionPolicyAllowedCountryList:
    return list(data)
