"""Generated from Smithy shape ``com.amazonaws.bedrock#CommitmentDuration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

CommitmentDuration: TypeAlias = Literal[
    "OneMonth",
    "SixMonths",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OneMonth",
        "SixMonths",
    )
)


def serialize_json(value: CommitmentDuration) -> str:
    return value


def deserialize_json(data: str) -> CommitmentDuration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommitmentDuration value: {data!r}")
    return cast(CommitmentDuration, data)
