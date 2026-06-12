"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetProfileErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batch_get_profile_error

BatchGetProfileErrorList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.batch_get_profile_error.BatchGetProfileError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetProfileErrorList) -> list:
    import aws_sdk_customer_profiles.types.batch_get_profile_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.batch_get_profile_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetProfileErrorList:
    import aws_sdk_customer_profiles.types.batch_get_profile_error

    out: BatchGetProfileErrorList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.batch_get_profile_error.deserialize_json(
                item
            )
        )
    return out
