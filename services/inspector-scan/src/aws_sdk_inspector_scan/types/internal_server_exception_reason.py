"""Generated from Smithy shape ``com.amazonaws.inspectorscan#InternalServerExceptionReason``."""

from typing import Literal, TypeAlias, cast

InternalServerExceptionReason: TypeAlias = Literal[
    "FAILED_TO_GENERATE_SBOM",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> InternalServerExceptionReason:
    return cast(InternalServerExceptionReason, data)
