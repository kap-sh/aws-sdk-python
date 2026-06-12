"""Generated from Smithy shape ``com.amazonaws.directoryservice#TargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

TargetType: TypeAlias = Literal["ACCOUNT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACCOUNT",))


def serialize_aws_json_1_1(value: TargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetType value: {data!r}")
    return cast(TargetType, data)
