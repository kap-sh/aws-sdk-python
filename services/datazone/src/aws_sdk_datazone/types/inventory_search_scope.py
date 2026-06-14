"""Generated from Smithy shape ``com.amazonaws.datazone#InventorySearchScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

InventorySearchScope: TypeAlias = Literal[
    "ASSET",
    "GLOSSARY",
    "GLOSSARY_TERM",
    "DATA_PRODUCT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET",
        "GLOSSARY",
        "GLOSSARY_TERM",
        "DATA_PRODUCT",
    )
)


def serialize_json(value: InventorySearchScope) -> str:
    return value


def deserialize_json(data: str) -> InventorySearchScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InventorySearchScope value: {data!r}")
    return cast(InventorySearchScope, data)
