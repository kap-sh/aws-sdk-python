"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SelectedAnalysisMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

SelectedAnalysisMethod: TypeAlias = Literal[
    "DIRECT_QUERY",
    "DIRECT_JOB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECT_QUERY",
        "DIRECT_JOB",
    )
)


def serialize_json(value: SelectedAnalysisMethod) -> str:
    return value


def deserialize_json(data: str) -> SelectedAnalysisMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelectedAnalysisMethod value: {data!r}")
    return cast(SelectedAnalysisMethod, data)
