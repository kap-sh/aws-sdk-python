"""Generated from Smithy shape ``com.amazonaws.evs#CheckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

CheckType: TypeAlias = Literal[
    "KEY_REUSE",
    "KEY_COVERAGE",
    "REACHABILITY",
    "HOST_COUNT",
    "VCENTER_REACHABILITY",
    "VCENTER_VM_SYNC",
    "VCENTER_VM_EVENT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEY_REUSE",
        "KEY_COVERAGE",
        "REACHABILITY",
        "HOST_COUNT",
        "VCENTER_REACHABILITY",
        "VCENTER_VM_SYNC",
        "VCENTER_VM_EVENT",
    )
)


def serialize_aws_json_1_0(value: CheckType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CheckType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CheckType value: {data!r}")
    return cast(CheckType, data)
