"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingDestinationTrafficState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_global_accelerator.errors import DeserializationError

CustomRoutingDestinationTrafficState: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_aws_json_1_1(value: CustomRoutingDestinationTrafficState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomRoutingDestinationTrafficState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomRoutingDestinationTrafficState value: {data!r}"
        )
    return cast(CustomRoutingDestinationTrafficState, data)
