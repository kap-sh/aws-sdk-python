"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainUpdateOperation``."""

from typing import Literal, TypeAlias, cast

FirewallDomainUpdateOperation: TypeAlias = Literal[
    "ADD",
    "REMOVE",
    "REPLACE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallDomainUpdateOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDomainUpdateOperation:
    return cast(FirewallDomainUpdateOperation, data)
