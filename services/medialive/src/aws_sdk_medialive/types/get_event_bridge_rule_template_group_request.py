"""Generated from Smithy shape ``com.amazonaws.medialive#GetEventBridgeRuleTemplateGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class GetEventBridgeRuleTemplateGroupRequest(TypedDict):
    identifier: "aws_sdk_medialive.types.__string.__string"
    """An eventbridge rule template group's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventBridgeRuleTemplateGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventBridgeRuleTemplateGroupRequest:
    out: GetEventBridgeRuleTemplateGroupRequest = {}  # type: ignore[typeddict-item]
    return out
