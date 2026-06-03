"""Generated from Smithy shape ``com.amazonaws.kms#RotationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.rotations_list_entry

RotationsList: TypeAlias = list[
    "aws_sdk_kms.types.rotations_list_entry.RotationsListEntry"
]
