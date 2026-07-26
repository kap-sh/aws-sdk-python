"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Batches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch

Batches: TypeAlias = list["capo_customer_profiles.types.batch.Batch"]


# --- restJson1 ser/de ---
def serialize_json(value: Batches) -> list:
    import capo_customer_profiles.types.batch

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.batch.serialize_json(item))
    return out


def deserialize_json(data: list) -> Batches:
    import capo_customer_profiles.types.batch

    out: Batches = []
    for item in data:
        out.append(capo_customer_profiles.types.batch.deserialize_json(item))
    return out
