"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionDestinationStatus``."""

from typing import Literal, TypeAlias, cast

IngestionDestinationStatus: TypeAlias = Literal[
    "Active",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionDestinationStatus) -> str:
    return value


def deserialize_json(data: str) -> IngestionDestinationStatus:
    return cast(IngestionDestinationStatus, data)
