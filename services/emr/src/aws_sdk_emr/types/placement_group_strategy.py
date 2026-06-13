"""Generated from Smithy shape ``com.amazonaws.emr#PlacementGroupStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

PlacementGroupStrategy: TypeAlias = Literal[
    "SPREAD",
    "PARTITION",
    "CLUSTER",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPREAD",
        "PARTITION",
        "CLUSTER",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: PlacementGroupStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlacementGroupStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlacementGroupStrategy value: {data!r}")
    return cast(PlacementGroupStrategy, data)
