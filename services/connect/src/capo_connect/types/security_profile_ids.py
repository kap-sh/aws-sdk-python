"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfileIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.security_profile_id

SecurityProfileIds: TypeAlias = list[
    "capo_connect.types.security_profile_id.SecurityProfileId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityProfileIds:
    return list(data)
