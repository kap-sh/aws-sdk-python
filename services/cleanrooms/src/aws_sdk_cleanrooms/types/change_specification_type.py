"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeSpecificationType``."""

from typing import Literal, TypeAlias, cast

ChangeSpecificationType: TypeAlias = Literal[
    "MEMBER",
    "COLLABORATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeSpecificationType) -> str:
    return value


def deserialize_json(data: str) -> ChangeSpecificationType:
    return cast(ChangeSpecificationType, data)
