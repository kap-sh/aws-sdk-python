"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketCorsRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.bucket_cors_rule

BucketCorsRules: TypeAlias = list[
    "capo_lightsail.types.bucket_cors_rule.BucketCorsRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketCorsRules) -> list:
    import capo_lightsail.types.bucket_cors_rule

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.bucket_cors_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BucketCorsRules:
    import capo_lightsail.types.bucket_cors_rule

    out: BucketCorsRules = []
    for item in data:
        out.append(capo_lightsail.types.bucket_cors_rule.deserialize_aws_json_1_1(item))
    return out
