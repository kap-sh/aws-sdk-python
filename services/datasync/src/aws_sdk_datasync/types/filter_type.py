"""Generated from Smithy shape ``com.amazonaws.datasync#FilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

FilterType: TypeAlias = Literal["SIMPLE_PATTERN",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SIMPLE_PATTERN",))


def serialize_aws_json_1_1(value: FilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterType value: {data!r}")
    return cast(FilterType, data)
