"""Generated from Smithy shape ``com.amazonaws.connect#AutomaticFailConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.reference_id


class AutomaticFailConfiguration(TypedDict):
    target_section: NotRequired["aws_sdk_connect.types.reference_id.ReferenceId"]
    """<p>The referenceId of the target section for auto failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomaticFailConfiguration) -> dict:
    out: dict = {}
    if "target_section" in value:
        out["TargetSection"] = value["target_section"]
    return out


def deserialize_json(data: dict) -> AutomaticFailConfiguration:
    out: AutomaticFailConfiguration = {}  # type: ignore[typeddict-item]
    if "TargetSection" in data:
        out["target_section"] = data["TargetSection"]
    return out
