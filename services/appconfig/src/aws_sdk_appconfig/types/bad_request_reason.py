"""Generated from Smithy shape ``com.amazonaws.appconfig#BadRequestReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

BadRequestReason: TypeAlias = Literal["InvalidConfiguration",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("InvalidConfiguration",))


def serialize_json(value: BadRequestReason) -> str:
    return value


def deserialize_json(data: str) -> BadRequestReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BadRequestReason value: {data!r}")
    return cast(BadRequestReason, data)
