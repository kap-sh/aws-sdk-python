"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ApplicationTagStatus``."""

from typing import Literal, TypeAlias, cast

ApplicationTagStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationTagStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationTagStatus:
    return cast(ApplicationTagStatus, data)
