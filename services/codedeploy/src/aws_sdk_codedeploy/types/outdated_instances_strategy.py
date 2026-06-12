"""Generated from Smithy shape ``com.amazonaws.codedeploy#OutdatedInstancesStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

OutdatedInstancesStrategy: TypeAlias = Literal[
    "UPDATE",
    "IGNORE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATE",
        "IGNORE",
    )
)


def serialize_aws_json_1_1(value: OutdatedInstancesStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutdatedInstancesStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutdatedInstancesStrategy value: {data!r}")
    return cast(OutdatedInstancesStrategy, data)
