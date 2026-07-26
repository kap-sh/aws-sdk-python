"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Permissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.permission

Permissions: TypeAlias = list["capo_elastic_transcoder.types.permission.Permission"]


# --- restJson1 ser/de ---
def serialize_json(value: Permissions) -> list:
    import capo_elastic_transcoder.types.permission

    out: list = []
    for item in value:
        out.append(capo_elastic_transcoder.types.permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> Permissions:
    import capo_elastic_transcoder.types.permission

    out: Permissions = []
    for item in data:
        out.append(capo_elastic_transcoder.types.permission.deserialize_json(item))
    return out
