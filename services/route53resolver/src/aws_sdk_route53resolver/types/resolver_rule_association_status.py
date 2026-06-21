"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRuleAssociationStatus``."""

from typing import Literal, TypeAlias, cast

ResolverRuleAssociationStatus: TypeAlias = Literal[
    "CREATING",
    "COMPLETE",
    "DELETING",
    "FAILED",
    "OVERRIDDEN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverRuleAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverRuleAssociationStatus:
    return cast(ResolverRuleAssociationStatus, data)
