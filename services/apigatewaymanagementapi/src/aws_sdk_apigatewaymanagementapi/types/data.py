"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#Data``."""

import base64
from typing import TypeAlias

"""<p>The data to be sent to the client specified by its connection id.</p>"""
Data: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: Data) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> Data:
    return base64.b64decode(data)
