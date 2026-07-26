"""Generated from Smithy shape ``com.amazonaws.iot#Buckets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.bucket

Buckets: TypeAlias = list["capo_iot.types.bucket.Bucket"]


# --- restJson1 ser/de ---
def serialize_json(value: Buckets) -> list:
    import capo_iot.types.bucket

    out: list = []
    for item in value:
        out.append(capo_iot.types.bucket.serialize_json(item))
    return out


def deserialize_json(data: list) -> Buckets:
    import capo_iot.types.bucket

    out: Buckets = []
    for item in data:
        out.append(capo_iot.types.bucket.deserialize_json(item))
    return out
