"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchPutProfileObjectErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch_put_profile_object_error_item

BatchPutProfileObjectErrorList: TypeAlias = list[
    "capo_customer_profiles.types.batch_put_profile_object_error_item.BatchPutProfileObjectErrorItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutProfileObjectErrorList) -> list:
    import capo_customer_profiles.types.batch_put_profile_object_error_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.batch_put_profile_object_error_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchPutProfileObjectErrorList:
    import capo_customer_profiles.types.batch_put_profile_object_error_item

    out: BatchPutProfileObjectErrorList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.batch_put_profile_object_error_item.deserialize_json(
                item
            )
        )
    return out
