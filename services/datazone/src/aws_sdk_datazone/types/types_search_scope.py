"""Generated from Smithy shape ``com.amazonaws.datazone#TypesSearchScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

TypesSearchScope: TypeAlias = Literal[
    "ASSET_TYPE",
    "FORM_TYPE",
    "LINEAGE_NODE_TYPE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET_TYPE",
        "FORM_TYPE",
        "LINEAGE_NODE_TYPE",
    )
)


def serialize_json(value: TypesSearchScope) -> str:
    return value


def deserialize_json(data: str) -> TypesSearchScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TypesSearchScope value: {data!r}")
    return cast(TypesSearchScope, data)
