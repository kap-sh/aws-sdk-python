"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociationType``."""

from typing import Literal, TypeAlias, cast

AssociationType: TypeAlias = Literal[
    "INHERITED",
    "APPLIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationType) -> str:
    return value


def deserialize_json(data: str) -> AssociationType:
    return cast(AssociationType, data)
