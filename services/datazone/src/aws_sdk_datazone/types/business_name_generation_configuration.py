"""Generated from Smithy shape ``com.amazonaws.datazone#BusinessNameGenerationConfiguration``."""

from typing import TypedDict
from typing_extensions import NotRequired


class BusinessNameGenerationConfiguration(TypedDict):
    enabled: NotRequired["bool"]
    """<p>Specifies whether the business name generation is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BusinessNameGenerationConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> BusinessNameGenerationConfiguration:
    out: BusinessNameGenerationConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
