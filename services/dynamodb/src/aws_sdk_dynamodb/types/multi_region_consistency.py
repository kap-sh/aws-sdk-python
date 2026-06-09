"""Generated from Smithy shape ``com.amazonaws.dynamodb#MultiRegionConsistency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

MultiRegionConsistency: TypeAlias = Literal[
    "EVENTUAL",
    "STRONG",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EVENTUAL",
        "STRONG",
    )
)


def serialize_aws_json_1_0(value: MultiRegionConsistency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MultiRegionConsistency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MultiRegionConsistency value: {data!r}")
    return cast(MultiRegionConsistency, data)
