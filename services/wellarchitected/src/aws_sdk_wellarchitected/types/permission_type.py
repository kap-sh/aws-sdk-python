"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PermissionType``."""

from typing import Literal, TypeAlias, cast

"""<p>Permission granted on a share request.</p>"""
PermissionType: TypeAlias = Literal[
    "READONLY",
    "CONTRIBUTOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionType) -> str:
    return value


def deserialize_json(data: str) -> PermissionType:
    return cast(PermissionType, data)
