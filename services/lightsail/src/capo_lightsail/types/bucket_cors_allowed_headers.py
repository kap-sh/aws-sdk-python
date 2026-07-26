"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketCorsAllowedHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.string

BucketCorsAllowedHeaders: TypeAlias = list["capo_lightsail.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketCorsAllowedHeaders) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BucketCorsAllowedHeaders:
    return list(data)
