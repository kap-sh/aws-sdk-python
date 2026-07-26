"""Generated from Smithy shape ``com.amazonaws.entityresolution#OutputAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.attribute_name


class OutputAttribute(TypedDict, closed=True):
    name: "capo_entityresolution.types.attribute_name.AttributeName"
    """<p>A name of a column to be written to the output. This must be an <code>InputField</code> name in the schema mapping.</p>"""
    hashed: NotRequired["bool"]
    """<p>Enables the ability to hash the column values in the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputAttribute) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "hashed" in value:
        out["hashed"] = value["hashed"]
    return out


def deserialize_json(data: dict) -> OutputAttribute:
    out: OutputAttribute = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("OutputAttribute.name required")
    if "hashed" in data:
        out["hashed"] = data["hashed"]
    return out
