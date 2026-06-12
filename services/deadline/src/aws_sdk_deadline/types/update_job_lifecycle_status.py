"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateJobLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

UpdateJobLifecycleStatus: TypeAlias = Literal["ARCHIVED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ARCHIVED",))


def serialize_json(value: UpdateJobLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateJobLifecycleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateJobLifecycleStatus value: {data!r}")
    return cast(UpdateJobLifecycleStatus, data)
