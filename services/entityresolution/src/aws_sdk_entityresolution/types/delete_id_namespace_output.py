"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteIdNamespaceOutput``."""

from typing import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError


class DeleteIdNamespaceOutput(TypedDict):
    message: "str"
    """<p>A successful operation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdNamespaceOutput) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteIdNamespaceOutput:
    out: DeleteIdNamespaceOutput = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DeleteIdNamespaceOutput.message required")
    return out
