"""Generated from Smithy shape ``com.amazonaws.amp#ComponentConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amp.types.string_map


class ComponentConfig(TypedDict):
    options: NotRequired["aws_sdk_amp.types.string_map.StringMap"]
    """<p>Configuration options for the scraper component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConfig) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_amp.types.string_map

        out["options"] = aws_sdk_amp.types.string_map.serialize_json(value["options"])
    return out


def deserialize_json(data: dict) -> ComponentConfig:
    out: ComponentConfig = {}  # type: ignore[typeddict-item]
    if "options" in data:
        import aws_sdk_amp.types.string_map

        out["options"] = aws_sdk_amp.types.string_map.deserialize_json(data["options"])
    return out
