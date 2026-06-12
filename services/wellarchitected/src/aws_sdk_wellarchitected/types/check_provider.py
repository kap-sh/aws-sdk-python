"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

CheckProvider: TypeAlias = Literal["TRUSTED_ADVISOR",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TRUSTED_ADVISOR",))


def serialize_json(value: CheckProvider) -> str:
    return value


def deserialize_json(data: str) -> CheckProvider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CheckProvider value: {data!r}")
    return cast(CheckProvider, data)
