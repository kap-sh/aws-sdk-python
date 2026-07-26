"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfigStatus``."""

from typing import Literal, TypeAlias, cast

ResolverQueryLogConfigStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverQueryLogConfigStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverQueryLogConfigStatus:
    return cast(ResolverQueryLogConfigStatus, data)
