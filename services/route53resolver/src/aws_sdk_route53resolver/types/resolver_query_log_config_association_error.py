"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfigAssociationError``."""

from typing import Literal, TypeAlias, cast

ResolverQueryLogConfigAssociationError: TypeAlias = Literal[
    "NONE",
    "DESTINATION_NOT_FOUND",
    "ACCESS_DENIED",
    "INTERNAL_SERVICE_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverQueryLogConfigAssociationError) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverQueryLogConfigAssociationError:
    return cast(ResolverQueryLogConfigAssociationError, data)
