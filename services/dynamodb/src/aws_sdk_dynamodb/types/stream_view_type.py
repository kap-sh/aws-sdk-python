"""Generated from Smithy shape ``com.amazonaws.dynamodb#StreamViewType``."""

from typing import Literal, TypeAlias

StreamViewType: TypeAlias = Literal[
    "NEW_IMAGE",
    "OLD_IMAGE",
    "NEW_AND_OLD_IMAGES",
    "KEYS_ONLY",
]
