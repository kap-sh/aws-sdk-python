"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppStatusType``."""

from typing import Literal, TypeAlias, cast

AppStatusType: TypeAlias = Literal[
    "Active",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppStatusType) -> str:
    return value


def deserialize_json(data: str) -> AppStatusType:
    return cast(AppStatusType, data)
