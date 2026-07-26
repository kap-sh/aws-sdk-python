"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ByoipCidrState``."""

from typing import Literal, TypeAlias, cast

ByoipCidrState: TypeAlias = Literal[
    "PENDING_PROVISIONING",
    "READY",
    "PENDING_ADVERTISING",
    "ADVERTISING",
    "PENDING_WITHDRAWING",
    "PENDING_DEPROVISIONING",
    "DEPROVISIONED",
    "FAILED_PROVISION",
    "FAILED_ADVERTISING",
    "FAILED_WITHDRAW",
    "FAILED_DEPROVISION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByoipCidrState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ByoipCidrState:
    return cast(ByoipCidrState, data)
