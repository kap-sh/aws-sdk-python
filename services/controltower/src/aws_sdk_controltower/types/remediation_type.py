"""Generated from Smithy shape ``com.amazonaws.controltower#RemediationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

RemediationType: TypeAlias = Literal["INHERITANCE_DRIFT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INHERITANCE_DRIFT",))


def serialize_json(value: RemediationType) -> str:
    return value


def deserialize_json(data: str) -> RemediationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RemediationType value: {data!r}")
    return cast(RemediationType, data)
