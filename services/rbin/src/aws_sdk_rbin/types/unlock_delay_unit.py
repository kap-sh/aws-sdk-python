"""Generated from Smithy shape ``com.amazonaws.rbin#UnlockDelayUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rbin.errors import DeserializationError

UnlockDelayUnit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DAYS",))


def serialize_json(value: UnlockDelayUnit) -> str:
    return value


def deserialize_json(data: str) -> UnlockDelayUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UnlockDelayUnit value: {data!r}")
    return cast(UnlockDelayUnit, data)
