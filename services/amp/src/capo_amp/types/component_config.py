"""Generated from Smithy shape ``com.amazonaws.amp#ComponentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.string_map


class ComponentConfig(TypedDict, closed=True):
    options: NotRequired["capo_amp.types.string_map.StringMap"]
    """<p>Configuration options for the scraper component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConfig) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_amp.types.string_map

        out["options"] = capo_amp.types.string_map.serialize_json(value["options"])
    return out


def deserialize_json(data: dict) -> ComponentConfig:
    out: ComponentConfig = {}  # type: ignore[typeddict-item]
    if "options" in data:
        import capo_amp.types.string_map

        out["options"] = capo_amp.types.string_map.deserialize_json(data["options"])
    return out
