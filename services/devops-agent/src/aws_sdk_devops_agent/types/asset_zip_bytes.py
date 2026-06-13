"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetZipBytes``."""

import base64
from typing import TypeAlias

"""<p>Zip file content as bytes</p>"""
AssetZipBytes: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AssetZipBytes) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AssetZipBytes:
    return base64.b64decode(data)
