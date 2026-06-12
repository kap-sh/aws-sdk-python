"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketCorsAllowedMethods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket_cors_allowed_method

BucketCorsAllowedMethods: TypeAlias = list[
    "aws_sdk_lightsail.types.bucket_cors_allowed_method.BucketCorsAllowedMethod"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketCorsAllowedMethods) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BucketCorsAllowedMethods:
    return list(data)
