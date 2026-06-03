"""Generated from Smithy shape ``com.amazonaws.kms#DryRunModifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import awd_sdk_kms.types.dry_run_modifier_type

DryRunModifierList: TypeAlias = list[
    "awd_sdk_kms.types.dry_run_modifier_type.DryRunModifierType"
]
