"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#EntityFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

EntityFilterName: TypeAlias = Literal[
    "NAME",
    "NAMESPACE",
    "SEMANTIC_TYPE_PATH",
    "REFERENCED_ENTITY_ID",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "NAMESPACE",
        "SEMANTIC_TYPE_PATH",
        "REFERENCED_ENTITY_ID",
    )
)


def serialize_aws_json_1_1(value: EntityFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityFilterName value: {data!r}")
    return cast(EntityFilterName, data)
