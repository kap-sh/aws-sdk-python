"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchPutProfileObjectResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batch_put_profile_object_response_item

BatchPutProfileObjectResponseList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.batch_put_profile_object_response_item.BatchPutProfileObjectResponseItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutProfileObjectResponseList) -> list:
    import aws_sdk_customer_profiles.types.batch_put_profile_object_response_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.batch_put_profile_object_response_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchPutProfileObjectResponseList:
    import aws_sdk_customer_profiles.types.batch_put_profile_object_response_item

    out: BatchPutProfileObjectResponseList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.batch_put_profile_object_response_item.deserialize_json(
                item
            )
        )
    return out
