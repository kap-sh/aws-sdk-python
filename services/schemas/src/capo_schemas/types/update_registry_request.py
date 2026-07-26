"""Generated from Smithy shape ``com.amazonaws.schemas#UpdateRegistryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string
    import capo_schemas.types.__string_min0_max256


class UpdateRegistryRequest(TypedDict, closed=True):
    description: NotRequired[
        "capo_schemas.types.__string_min0_max256.__stringMin0Max256"
    ]
    """<p>The description of the registry to update.</p>"""
    registry_name: "capo_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateRegistryRequest:
    out: UpdateRegistryRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
