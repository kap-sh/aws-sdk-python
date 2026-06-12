"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceImportStrategyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ResourceImportStrategyType: TypeAlias = Literal[
    "AddOnly",
    "ReplaceAll",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AddOnly",
        "ReplaceAll",
    )
)


def serialize_json(value: ResourceImportStrategyType) -> str:
    return value


def deserialize_json(data: str) -> ResourceImportStrategyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceImportStrategyType value: {data!r}"
        )
    return cast(ResourceImportStrategyType, data)
