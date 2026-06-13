"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportBodyBlob``."""

import base64
from typing import TypeAlias

AssetBundleImportBodyBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportBodyBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AssetBundleImportBodyBlob:
    return base64.b64decode(data)
