"""Generated from Smithy shape ``com.amazonaws.connect#AllowedAccessControlTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.security_profile_policy_key
    import capo_connect.types.security_profile_policy_value

AllowedAccessControlTags: TypeAlias = dict[
    "capo_connect.types.security_profile_policy_key.SecurityProfilePolicyKey",
    "capo_connect.types.security_profile_policy_value.SecurityProfilePolicyValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AllowedAccessControlTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AllowedAccessControlTags:
    out: AllowedAccessControlTags = {}
    for key, value in data.items():
        out[key] = value
    return out
