"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#EngineVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mwaa_serverless.errors import DeserializationError

EngineVersion: TypeAlias = Literal[1,]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[int] = frozenset((1,))


def serialize_aws_json_1_0(value: EngineVersion) -> int:
    return value


def deserialize_aws_json_1_0(data: int) -> EngineVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngineVersion value: {data!r}")
    return cast(EngineVersion, data)
