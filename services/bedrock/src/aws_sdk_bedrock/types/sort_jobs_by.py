"""Generated from Smithy shape ``com.amazonaws.bedrock#SortJobsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

SortJobsBy: TypeAlias = Literal["CreationTime",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreationTime",))


def serialize_json(value: SortJobsBy) -> str:
    return value


def deserialize_json(data: str) -> SortJobsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortJobsBy value: {data!r}")
    return cast(SortJobsBy, data)
