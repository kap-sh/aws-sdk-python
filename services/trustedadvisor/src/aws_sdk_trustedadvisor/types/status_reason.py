"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#StatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

StatusReason: TypeAlias = Literal["no_data_ok",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("no_data_ok",))


def serialize_json(value: StatusReason) -> str:
    return value


def deserialize_json(data: str) -> StatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusReason value: {data!r}")
    return cast(StatusReason, data)
