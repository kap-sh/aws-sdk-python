"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.security_profile_item

SecurityProfiles: TypeAlias = list[
    "aws_sdk_connect.types.security_profile_item.SecurityProfileItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfiles) -> list:
    import aws_sdk_connect.types.security_profile_item

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.security_profile_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityProfiles:
    import aws_sdk_connect.types.security_profile_item

    out: SecurityProfiles = []
    for item in data:
        out.append(aws_sdk_connect.types.security_profile_item.deserialize_json(item))
    return out
