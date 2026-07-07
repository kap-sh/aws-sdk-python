"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantCapabilityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.assistant_capability_type


class AssistantCapabilityConfiguration(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_qconnect.types.assistant_capability_type.AssistantCapabilityType"
    ]
    """<p>The type of Amazon Q in Connect assistant capability. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantCapabilityConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AssistantCapabilityConfiguration:
    out: AssistantCapabilityConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    return out
