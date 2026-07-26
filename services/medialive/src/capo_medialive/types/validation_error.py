"""Generated from Smithy shape ``com.amazonaws.medialive#ValidationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class ValidationError(TypedDict, closed=True):
    element_path: NotRequired["capo_medialive.types.__string.__string"]
    """Path to the source of the error."""
    error_message: NotRequired["capo_medialive.types.__string.__string"]
    """The error message."""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationError) -> dict:
    out: dict = {}
    if "element_path" in value:
        out["elementPath"] = value["element_path"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ValidationError:
    out: ValidationError = {}  # type: ignore[typeddict-item]
    if "elementPath" in data:
        out["element_path"] = data["elementPath"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
