"""Generated from Smithy shape ``com.amazonaws.workspaces#Platform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

Platform: TypeAlias = Literal["WINDOWS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WINDOWS",))


def serialize_aws_json_1_1(value: Platform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Platform:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Platform value: {data!r}")
    return cast(Platform, data)
