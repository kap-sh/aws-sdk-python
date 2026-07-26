"""Generated from Smithy shape ``com.amazonaws.backup#ProtectedResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.protected_resource

ProtectedResourcesList: TypeAlias = list[
    "capo_backup.types.protected_resource.ProtectedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedResourcesList) -> list:
    import capo_backup.types.protected_resource

    out: list = []
    for item in value:
        out.append(capo_backup.types.protected_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProtectedResourcesList:
    import capo_backup.types.protected_resource

    out: ProtectedResourcesList = []
    for item in data:
        out.append(capo_backup.types.protected_resource.deserialize_json(item))
    return out
