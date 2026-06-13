"""Generated from Smithy shape ``com.amazonaws.neptunedata#ReportAsText``."""

import base64
from typing import TypeAlias

ReportAsText: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: ReportAsText) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> ReportAsText:
    return base64.b64decode(data)
