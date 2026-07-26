"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetCalculatedAttributeForProfileErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error

BatchGetCalculatedAttributeForProfileErrorList: TypeAlias = list[
    "capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error.BatchGetCalculatedAttributeForProfileError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCalculatedAttributeForProfileErrorList) -> list:
    import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetCalculatedAttributeForProfileErrorList:
    import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error

    out: BatchGetCalculatedAttributeForProfileErrorList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_error.deserialize_json(
                item
            )
        )
    return out
