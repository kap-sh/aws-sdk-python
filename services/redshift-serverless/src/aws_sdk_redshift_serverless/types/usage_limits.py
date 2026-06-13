"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UsageLimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.usage_limit

UsageLimits: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.usage_limit.UsageLimit"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageLimits) -> list:
    import aws_sdk_redshift_serverless.types.usage_limit

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.usage_limit.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsageLimits:
    import aws_sdk_redshift_serverless.types.usage_limit

    out: UsageLimits = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.usage_limit.deserialize_aws_json_1_1(item)
        )
    return out
