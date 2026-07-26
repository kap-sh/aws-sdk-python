"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetProfileErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch_get_profile_error

BatchGetProfileErrorList: TypeAlias = list[
    "capo_customer_profiles.types.batch_get_profile_error.BatchGetProfileError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetProfileErrorList) -> list:
    import capo_customer_profiles.types.batch_get_profile_error

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.batch_get_profile_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetProfileErrorList:
    import capo_customer_profiles.types.batch_get_profile_error

    out: BatchGetProfileErrorList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.batch_get_profile_error.deserialize_json(item)
        )
    return out
