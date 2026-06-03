"""Generated from Smithy shape ``com.amazonaws.kms#RotationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import awd_sdk_kms.types.rotations_list_entry

RotationsList: TypeAlias = list[
    "awd_sdk_kms.types.rotations_list_entry.RotationsListEntry"
]
