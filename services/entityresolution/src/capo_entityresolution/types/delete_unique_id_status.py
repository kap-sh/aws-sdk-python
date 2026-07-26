"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteUniqueIdStatus``."""

from typing import Literal, TypeAlias, cast

DeleteUniqueIdStatus: TypeAlias = Literal[
    "COMPLETED",
    "ACCEPTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUniqueIdStatus) -> str:
    return value


def deserialize_json(data: str) -> DeleteUniqueIdStatus:
    return cast(DeleteUniqueIdStatus, data)
