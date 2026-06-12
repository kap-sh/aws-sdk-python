"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.profile

ProfileList: TypeAlias = list["aws_sdk_customer_profiles.types.profile.Profile"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileList) -> list:
    import aws_sdk_customer_profiles.types.profile

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileList:
    import aws_sdk_customer_profiles.types.profile

    out: ProfileList = []
    for item in data:
        out.append(aws_sdk_customer_profiles.types.profile.deserialize_json(item))
    return out
