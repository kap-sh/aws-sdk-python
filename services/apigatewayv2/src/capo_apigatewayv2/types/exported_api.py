"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ExportedApi``."""

import base64
from typing import TypeAlias

"""<p>Represents an exported definition of an API in a particular output format, for example, YAML. The API is serialized to the requested specification, for example, OpenAPI 3.0.</p>"""
ExportedApi: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: ExportedApi) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> ExportedApi:
    return base64.b64decode(data)
