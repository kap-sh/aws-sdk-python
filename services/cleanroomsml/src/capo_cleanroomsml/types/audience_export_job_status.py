"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceExportJobStatus``."""

from typing import Literal, TypeAlias, cast

AudienceExportJobStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceExportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AudienceExportJobStatus:
    return cast(AudienceExportJobStatus, data)
