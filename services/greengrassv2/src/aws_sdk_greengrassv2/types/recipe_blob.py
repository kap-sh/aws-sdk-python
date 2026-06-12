"""Generated from Smithy shape ``com.amazonaws.greengrassv2#RecipeBlob``."""

import base64
from typing import TypeAlias

RecipeBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: RecipeBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> RecipeBlob:
    return base64.b64decode(data)
