"""Generated from Smithy shape ``com.amazonaws.entityresolution#ResolutionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

ResolutionType: TypeAlias = Literal[
    "RULE_MATCHING",
    "ML_MATCHING",
    "PROVIDER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RULE_MATCHING",
        "ML_MATCHING",
        "PROVIDER",
    )
)


def serialize_json(value: ResolutionType) -> str:
    return value


def deserialize_json(data: str) -> ResolutionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolutionType value: {data!r}")
    return cast(ResolutionType, data)
