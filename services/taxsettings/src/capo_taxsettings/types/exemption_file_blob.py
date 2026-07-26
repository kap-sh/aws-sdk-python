"""Generated from Smithy shape ``com.amazonaws.taxsettings#ExemptionFileBlob``."""

import base64
from typing import TypeAlias

ExemptionFileBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: ExemptionFileBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> ExemptionFileBlob:
    return base64.b64decode(data)
