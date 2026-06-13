"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomNarrativeOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.narrative_string


class CustomNarrativeOptions(TypedDict):
    narrative: "aws_sdk_quicksight.types.narrative_string.NarrativeString"
    """<p>The string input of custom narrative.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomNarrativeOptions) -> dict:
    out: dict = {}
    out["Narrative"] = value["narrative"]
    return out


def deserialize_json(data: dict) -> CustomNarrativeOptions:
    out: CustomNarrativeOptions = {}  # type: ignore[typeddict-item]
    if "Narrative" in data:
        out["narrative"] = data["Narrative"]
    else:
        raise DeserializationError("CustomNarrativeOptions.narrative required")
    return out
