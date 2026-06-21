"""Generated from Smithy shape ``com.amazonaws.lambda#InvocationType``."""

from typing import Literal, TypeAlias, cast

InvocationType: TypeAlias = Literal[
    "Event",
    "RequestResponse",
    "DryRun",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvocationType) -> str:
    return value


def deserialize_json(data: str) -> InvocationType:
    return cast(InvocationType, data)
