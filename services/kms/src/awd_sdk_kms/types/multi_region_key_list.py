"""Generated from Smithy shape ``com.amazonaws.kms#MultiRegionKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import awd_sdk_kms.types.multi_region_key

MultiRegionKeyList: TypeAlias = list[
    "awd_sdk_kms.types.multi_region_key.MultiRegionKey"
]
