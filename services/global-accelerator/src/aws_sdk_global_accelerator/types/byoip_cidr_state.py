"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ByoipCidrState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_global_accelerator.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: ByoipCidrState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ByoipCidrState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ByoipCidrState value: {data!r}")
    return cast(ByoipCidrState, data)
