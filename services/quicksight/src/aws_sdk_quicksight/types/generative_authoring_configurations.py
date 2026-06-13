"""Generated from Smithy shape ``com.amazonaws.quicksight#GenerativeAuthoringConfigurations``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class GenerativeAuthoringConfigurations(TypedDict):
    enabled: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>The generative BI authoring settings of an embedded Quick Sight console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerativeAuthoringConfigurations) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> GenerativeAuthoringConfigurations:
    out: GenerativeAuthoringConfigurations = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
