"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DICOMAttribute``."""

import base64
from typing import TypeAlias

DICOMAttribute: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: DICOMAttribute) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> DICOMAttribute:
    return base64.b64decode(data)
