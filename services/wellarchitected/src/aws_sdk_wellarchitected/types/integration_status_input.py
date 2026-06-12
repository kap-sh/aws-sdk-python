"""Generated from Smithy shape ``com.amazonaws.wellarchitected#IntegrationStatusInput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

IntegrationStatusInput: TypeAlias = Literal["NOT_CONFIGURED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NOT_CONFIGURED",))


def serialize_json(value: IntegrationStatusInput) -> str:
    return value


def deserialize_json(data: str) -> IntegrationStatusInput:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationStatusInput value: {data!r}")
    return cast(IntegrationStatusInput, data)
