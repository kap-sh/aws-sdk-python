"""Generated from Smithy shape ``com.amazonaws.wellarchitected#IntegratingService``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

IntegratingService: TypeAlias = Literal["JIRA",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("JIRA",))


def serialize_json(value: IntegratingService) -> str:
    return value


def deserialize_json(data: str) -> IntegratingService:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegratingService value: {data!r}")
    return cast(IntegratingService, data)
