"""Generated from Smithy shape ``com.amazonaws.mediastore#CorsPolicy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.cors_rule

CorsPolicy: TypeAlias = list["aws_sdk_mediastore.types.cors_rule.CorsRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CorsPolicy) -> list:
    import aws_sdk_mediastore.types.cors_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_mediastore.types.cors_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CorsPolicy:
    import aws_sdk_mediastore.types.cors_rule

    out: CorsPolicy = []
    for item in data:
        out.append(aws_sdk_mediastore.types.cors_rule.deserialize_aws_json_1_1(item))
    return out
