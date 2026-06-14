"""Generated from Smithy shape ``com.amazonaws.datazone#JobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

JobType: TypeAlias = Literal["LINEAGE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LINEAGE",))


def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobType value: {data!r}")
    return cast(JobType, data)
