"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ProfileDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.profile_detail

ProfileDetails: TypeAlias = list[
    "aws_sdk_rolesanywhere.types.profile_detail.ProfileDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileDetails) -> list:
    import aws_sdk_rolesanywhere.types.profile_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_rolesanywhere.types.profile_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileDetails:
    import aws_sdk_rolesanywhere.types.profile_detail

    out: ProfileDetails = []
    for item in data:
        out.append(aws_sdk_rolesanywhere.types.profile_detail.deserialize_json(item))
    return out
