"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowDedupeStrategyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationFlowDedupeStrategyType: TypeAlias = Literal["FIELD_PRIORITY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FIELD_PRIORITY",))


def serialize_json(value: DataIntegrationFlowDedupeStrategyType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowDedupeStrategyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationFlowDedupeStrategyType value: {data!r}"
        )
    return cast(DataIntegrationFlowDedupeStrategyType, data)
