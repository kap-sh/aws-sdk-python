"""Generated from Smithy shape ``com.amazonaws.mpa#PolicyStatus``."""

from typing import Literal, TypeAlias, cast

PolicyStatus: TypeAlias = Literal[
    "ATTACHABLE",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyStatus) -> str:
    return value


def deserialize_json(data: str) -> PolicyStatus:
    return cast(PolicyStatus, data)
