"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainListStatus``."""

from typing import Literal, TypeAlias, cast

FirewallDomainListStatus: TypeAlias = Literal[
    "COMPLETE",
    "COMPLETE_IMPORT_FAILED",
    "IMPORTING",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallDomainListStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDomainListStatus:
    return cast(FirewallDomainListStatus, data)
