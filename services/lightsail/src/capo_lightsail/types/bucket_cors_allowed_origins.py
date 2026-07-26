"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketCorsAllowedOrigins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.string

BucketCorsAllowedOrigins: TypeAlias = list["capo_lightsail.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketCorsAllowedOrigins) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BucketCorsAllowedOrigins:
    return list(data)
