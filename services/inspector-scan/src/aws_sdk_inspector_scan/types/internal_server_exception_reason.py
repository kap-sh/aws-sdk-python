"""Generated from Smithy shape ``com.amazonaws.inspectorscan#InternalServerExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector_scan.errors import DeserializationError

InternalServerExceptionReason: TypeAlias = Literal[
    "FAILED_TO_GENERATE_SBOM",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED_TO_GENERATE_SBOM",
        "OTHER",
    )
)


def serialize_json(value: InternalServerExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> InternalServerExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InternalServerExceptionReason value: {data!r}"
        )
    return cast(InternalServerExceptionReason, data)
