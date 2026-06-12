"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingAcceleratorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_global_accelerator.errors import DeserializationError

CustomRoutingAcceleratorStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: CustomRoutingAcceleratorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomRoutingAcceleratorStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomRoutingAcceleratorStatus value: {data!r}"
        )
    return cast(CustomRoutingAcceleratorStatus, data)
