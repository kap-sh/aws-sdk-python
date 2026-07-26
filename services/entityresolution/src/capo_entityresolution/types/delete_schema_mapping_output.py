"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteSchemaMappingOutput``."""

from typing_extensions import TypedDict

from capo_entityresolution.errors import DeserializationError


class DeleteSchemaMappingOutput(TypedDict, closed=True):
    message: "str"
    """<p>A successful operation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaMappingOutput) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteSchemaMappingOutput:
    out: DeleteSchemaMappingOutput = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DeleteSchemaMappingOutput.message required")
    return out
