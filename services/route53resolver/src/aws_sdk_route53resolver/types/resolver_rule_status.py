"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRuleStatus``."""

from typing import Literal, TypeAlias, cast

ResolverRuleStatus: TypeAlias = Literal[
    "COMPLETE",
    "DELETING",
    "UPDATING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverRuleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverRuleStatus:
    return cast(ResolverRuleStatus, data)
