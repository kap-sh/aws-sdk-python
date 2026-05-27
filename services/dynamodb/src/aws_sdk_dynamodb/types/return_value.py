"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReturnValue``."""

from typing import Literal, TypeAlias

ReturnValue: TypeAlias = Literal[
    "NONE",
    "ALL_OLD",
    "UPDATED_OLD",
    "ALL_NEW",
    "UPDATED_NEW",
]
