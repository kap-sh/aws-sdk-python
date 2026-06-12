"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AssessmentInvoker``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

AssessmentInvoker: TypeAlias = Literal[
    "User",
    "System",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "User",
        "System",
    )
)


def serialize_json(value: AssessmentInvoker) -> str:
    return value


def deserialize_json(data: str) -> AssessmentInvoker:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssessmentInvoker value: {data!r}")
    return cast(AssessmentInvoker, data)
