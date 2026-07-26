"""Generated from Smithy shape ``com.amazonaws.opensearch#ApplicationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.application_status

ApplicationStatuses: TypeAlias = list[
    "capo_opensearch.types.application_status.ApplicationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationStatuses) -> list:
    import capo_opensearch.types.application_status

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.application_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationStatuses:
    import capo_opensearch.types.application_status

    out: ApplicationStatuses = []
    for item in data:
        out.append(capo_opensearch.types.application_status.deserialize_json(item))
    return out
