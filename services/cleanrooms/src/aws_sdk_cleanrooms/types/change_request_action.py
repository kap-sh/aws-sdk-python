"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeRequestAction``."""

from typing import Literal, TypeAlias, cast

ChangeRequestAction: TypeAlias = Literal[
    "APPROVE",
    "DENY",
    "CANCEL",
    "COMMIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeRequestAction) -> str:
    return value


def deserialize_json(data: str) -> ChangeRequestAction:
    return cast(ChangeRequestAction, data)
