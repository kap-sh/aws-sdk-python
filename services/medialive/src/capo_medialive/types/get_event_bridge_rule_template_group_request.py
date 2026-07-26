"""Generated from Smithy shape ``com.amazonaws.medialive#GetEventBridgeRuleTemplateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class GetEventBridgeRuleTemplateGroupRequest(TypedDict, closed=True):
    identifier: "capo_medialive.types.__string.__string"
    """An eventbridge rule template group's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventBridgeRuleTemplateGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventBridgeRuleTemplateGroupRequest:
    out: GetEventBridgeRuleTemplateGroupRequest = {}  # type: ignore[typeddict-item]
    return out
