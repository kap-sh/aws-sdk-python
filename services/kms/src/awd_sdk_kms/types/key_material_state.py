"""Generated from Smithy shape ``com.amazonaws.kms#KeyMaterialState``."""

from typing import Literal, TypeAlias

KeyMaterialState: TypeAlias = Literal[
    "NON_CURRENT",
    "CURRENT",
    "PENDING_ROTATION",
    "PENDING_MULTI_REGION_IMPORT_AND_ROTATION",
]
