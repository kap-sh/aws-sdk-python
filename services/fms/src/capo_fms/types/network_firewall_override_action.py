"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallOverrideAction``."""

from typing import Literal, TypeAlias, cast

NetworkFirewallOverrideAction: TypeAlias = Literal["DROP_TO_ALERT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallOverrideAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkFirewallOverrideAction:
    return cast(NetworkFirewallOverrideAction, data)
