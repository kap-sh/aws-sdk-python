"""Generated from Smithy shape ``com.amazonaws.emr#ExecutionEngineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

ExecutionEngineType: TypeAlias = Literal["EMR",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EMR",))


def serialize_aws_json_1_1(value: ExecutionEngineType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionEngineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionEngineType value: {data!r}")
    return cast(ExecutionEngineType, data)
