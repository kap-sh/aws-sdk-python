"""Generated from Smithy shape ``com.amazonaws.panorama#ValidationExceptionErrorArgument``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.string


class ValidationExceptionErrorArgument(TypedDict, closed=True):
    name: "capo_panorama.types.string.String"
    """<p>The argument's name.</p>"""
    value: "capo_panorama.types.string.String"
    """<p>The argument's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionErrorArgument) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionErrorArgument:
    out: ValidationExceptionErrorArgument = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ValidationExceptionErrorArgument.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ValidationExceptionErrorArgument.value required")
    return out
