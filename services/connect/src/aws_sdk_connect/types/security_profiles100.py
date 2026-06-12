"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfiles100``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.security_profile_item

SecurityProfiles100: TypeAlias = list[
    "aws_sdk_connect.types.security_profile_item.SecurityProfileItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfiles100) -> list:
    import aws_sdk_connect.types.security_profile_item

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.security_profile_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityProfiles100:
    import aws_sdk_connect.types.security_profile_item

    out: SecurityProfiles100 = []
    for item in data:
        out.append(aws_sdk_connect.types.security_profile_item.deserialize_json(item))
    return out
