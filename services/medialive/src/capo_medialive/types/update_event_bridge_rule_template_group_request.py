"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateEventBridgeRuleTemplateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.__string_min0_max1024


class UpdateEventBridgeRuleTemplateGroupRequest(TypedDict, closed=True):
    description: NotRequired[
        "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    identifier: "capo_medialive.types.__string.__string"
    """An eventbridge rule template group's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventBridgeRuleTemplateGroupRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateEventBridgeRuleTemplateGroupRequest:
    out: UpdateEventBridgeRuleTemplateGroupRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
