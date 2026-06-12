"""Generated from Smithy shape ``com.amazonaws.configservice#SortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

SortBy: TypeAlias = Literal["SCORE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SCORE",))


def serialize_aws_json_1_1(value: SortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortBy value: {data!r}")
    return cast(SortBy, data)
