"""Generated from Smithy shape ``com.amazonaws.securitylake#SourceCollectionStatus``."""

from typing import Literal, TypeAlias, cast

SourceCollectionStatus: TypeAlias = Literal[
    "COLLECTING",
    "MISCONFIGURED",
    "NOT_COLLECTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceCollectionStatus) -> str:
    return value


def deserialize_json(data: str) -> SourceCollectionStatus:
    return cast(SourceCollectionStatus, data)
