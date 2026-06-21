"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallStatusValue``."""

from typing import Literal, TypeAlias, cast

FirewallStatusValue: TypeAlias = Literal[
    "PROVISIONING",
    "DELETING",
    "READY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallStatusValue) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FirewallStatusValue:
    return cast(FirewallStatusValue, data)
