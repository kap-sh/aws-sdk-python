"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowRuleDefinitionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

IdMappingWorkflowRuleDefinitionType: TypeAlias = Literal[
    "SOURCE",
    "TARGET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOURCE",
        "TARGET",
    )
)


def serialize_json(value: IdMappingWorkflowRuleDefinitionType) -> str:
    return value


def deserialize_json(data: str) -> IdMappingWorkflowRuleDefinitionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IdMappingWorkflowRuleDefinitionType value: {data!r}"
        )
    return cast(IdMappingWorkflowRuleDefinitionType, data)
