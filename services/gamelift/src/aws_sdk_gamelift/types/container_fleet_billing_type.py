"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetBillingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ContainerFleetBillingType: TypeAlias = Literal[
    "ON_DEMAND",
    "SPOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "SPOT",
    )
)


def serialize_aws_json_1_1(value: ContainerFleetBillingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerFleetBillingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerFleetBillingType value: {data!r}")
    return cast(ContainerFleetBillingType, data)
