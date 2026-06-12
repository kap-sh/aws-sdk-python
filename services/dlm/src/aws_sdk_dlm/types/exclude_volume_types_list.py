"""Generated from Smithy shape ``com.amazonaws.dlm#ExcludeVolumeTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.volume_type_values

ExcludeVolumeTypesList: TypeAlias = list[
    "aws_sdk_dlm.types.volume_type_values.VolumeTypeValues"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExcludeVolumeTypesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExcludeVolumeTypesList:
    return list(data)
