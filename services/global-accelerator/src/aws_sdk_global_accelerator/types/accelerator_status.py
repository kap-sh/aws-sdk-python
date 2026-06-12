"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AcceleratorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_global_accelerator.errors import DeserializationError

AcceleratorStatus: TypeAlias = Literal[
    "DEPLOYED",
    "IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEPLOYED",
        "IN_PROGRESS",
    )
)


def serialize_aws_json_1_1(value: AcceleratorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceleratorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceleratorStatus value: {data!r}")
    return cast(AcceleratorStatus, data)
