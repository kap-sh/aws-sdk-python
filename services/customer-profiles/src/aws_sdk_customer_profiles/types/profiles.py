"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Profiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.profile_query_result

Profiles: TypeAlias = list[
    "aws_sdk_customer_profiles.types.profile_query_result.ProfileQueryResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: Profiles) -> list:
    import aws_sdk_customer_profiles.types.profile_query_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.profile_query_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Profiles:
    import aws_sdk_customer_profiles.types.profile_query_result

    out: Profiles = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.profile_query_result.deserialize_json(item)
        )
    return out
