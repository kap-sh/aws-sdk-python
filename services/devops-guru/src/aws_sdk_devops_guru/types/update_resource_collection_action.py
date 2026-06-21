"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateResourceCollectionAction``."""

from typing import Literal, TypeAlias, cast

UpdateResourceCollectionAction: TypeAlias = Literal[
    "ADD",
    "REMOVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceCollectionAction) -> str:
    return value


def deserialize_json(data: str) -> UpdateResourceCollectionAction:
    return cast(UpdateResourceCollectionAction, data)
