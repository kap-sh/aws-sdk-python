"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotTypeFilterName: TypeAlias = Literal[
    "SlotTypeName",
    "ExternalSourceType",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SlotTypeName",
        "ExternalSourceType",
    )
)


def serialize_json(value: SlotTypeFilterName) -> str:
    return value


def deserialize_json(data: str) -> SlotTypeFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotTypeFilterName value: {data!r}")
    return cast(SlotTypeFilterName, data)
