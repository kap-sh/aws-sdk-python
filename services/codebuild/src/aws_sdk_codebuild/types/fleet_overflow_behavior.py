"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetOverflowBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

FleetOverflowBehavior: TypeAlias = Literal[
    "QUEUE",
    "ON_DEMAND",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUE",
        "ON_DEMAND",
    )
)


def serialize_aws_json_1_1(value: FleetOverflowBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetOverflowBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetOverflowBehavior value: {data!r}")
    return cast(FleetOverflowBehavior, data)
