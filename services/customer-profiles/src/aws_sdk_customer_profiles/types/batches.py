"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Batches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batch

Batches: TypeAlias = list["aws_sdk_customer_profiles.types.batch.Batch"]


# --- restJson1 ser/de ---
def serialize_json(value: Batches) -> list:
    import aws_sdk_customer_profiles.types.batch

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.batch.serialize_json(item))
    return out


def deserialize_json(data: list) -> Batches:
    import aws_sdk_customer_profiles.types.batch

    out: Batches = []
    for item in data:
        out.append(aws_sdk_customer_profiles.types.batch.deserialize_json(item))
    return out
