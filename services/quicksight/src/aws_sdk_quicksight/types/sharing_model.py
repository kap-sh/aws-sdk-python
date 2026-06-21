"""Generated from Smithy shape ``com.amazonaws.quicksight#SharingModel``."""

from typing import Literal, TypeAlias, cast

SharingModel: TypeAlias = Literal[
    "ACCOUNT",
    "NAMESPACE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SharingModel) -> str:
    return value


def deserialize_json(data: str) -> SharingModel:
    return cast(SharingModel, data)
