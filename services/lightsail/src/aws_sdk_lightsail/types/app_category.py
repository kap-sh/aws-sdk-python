"""Generated from Smithy shape ``com.amazonaws.lightsail#AppCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

AppCategory: TypeAlias = Literal["LfR",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LfR",))


def serialize_aws_json_1_1(value: AppCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppCategory value: {data!r}")
    return cast(AppCategory, data)
