"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteEventBridgeRuleTemplateGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteEventBridgeRuleTemplateGroupRequest(TypedDict):
    identifier: "aws_sdk_medialive.types.__string.__string"
    """An eventbridge rule template group's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventBridgeRuleTemplateGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventBridgeRuleTemplateGroupRequest:
    out: DeleteEventBridgeRuleTemplateGroupRequest = {}  # type: ignore[typeddict-item]
    return out
