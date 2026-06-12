"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileTypeValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.profile_type

ProfileTypeValues: TypeAlias = list[
    "aws_sdk_customer_profiles.types.profile_type.ProfileType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTypeValues) -> list:
    import aws_sdk_customer_profiles.types.profile_type

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.profile_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileTypeValues:
    import aws_sdk_customer_profiles.types.profile_type

    out: ProfileTypeValues = []
    for item in data:
        out.append(aws_sdk_customer_profiles.types.profile_type.deserialize_json(item))
    return out
