"""Generated from Smithy shape ``com.amazonaws.medialive#GetEventBridgeRuleTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class GetEventBridgeRuleTemplateRequest(TypedDict):
    identifier: "aws_sdk_medialive.types.__string.__string"
    """An eventbridge rule template's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventBridgeRuleTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventBridgeRuleTemplateRequest:
    out: GetEventBridgeRuleTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
