"""Generated from Smithy shape ``com.amazonaws.efs#AccessPointDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_efs.types.access_point_description

AccessPointDescriptions: TypeAlias = list[
    "capo_efs.types.access_point_description.AccessPointDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPointDescriptions) -> list:
    import capo_efs.types.access_point_description

    out: list = []
    for item in value:
        out.append(capo_efs.types.access_point_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessPointDescriptions:
    import capo_efs.types.access_point_description

    out: AccessPointDescriptions = []
    for item in data:
        out.append(capo_efs.types.access_point_description.deserialize_json(item))
    return out
