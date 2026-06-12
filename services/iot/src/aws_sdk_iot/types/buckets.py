"""Generated from Smithy shape ``com.amazonaws.iot#Buckets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.bucket

Buckets: TypeAlias = list["aws_sdk_iot.types.bucket.Bucket"]


# --- restJson1 ser/de ---
def serialize_json(value: Buckets) -> list:
    import aws_sdk_iot.types.bucket

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.bucket.serialize_json(item))
    return out


def deserialize_json(data: list) -> Buckets:
    import aws_sdk_iot.types.bucket

    out: Buckets = []
    for item in data:
        out.append(aws_sdk_iot.types.bucket.deserialize_json(item))
    return out
