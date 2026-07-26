"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ServiceOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string


class ServiceOverride(TypedDict, closed=True):
    message: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Details about the service override that MediaConvert has applied."""
    name: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The name of the setting that MediaConvert has applied an override to."""
    override_value: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The current value of the service override that MediaConvert has applied."""
    value: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The value of the setting that you configured, prior to any overrides that MediaConvert has applied."""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceOverride) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "name" in value:
        out["name"] = value["name"]
    if "override_value" in value:
        out["overrideValue"] = value["override_value"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ServiceOverride:
    out: ServiceOverride = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "name" in data:
        out["name"] = data["name"]
    if "overrideValue" in data:
        out["override_value"] = data["overrideValue"]
    if "value" in data:
        out["value"] = data["value"]
    return out
