"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfigAssociationStatus``."""

from typing import Literal, TypeAlias, cast

ResolverQueryLogConfigAssociationStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "ACTION_NEEDED",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverQueryLogConfigAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverQueryLogConfigAssociationStatus:
    return cast(ResolverQueryLogConfigAssociationStatus, data)
