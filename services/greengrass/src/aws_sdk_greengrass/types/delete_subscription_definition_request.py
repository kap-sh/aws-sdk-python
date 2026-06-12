"""Generated from Smithy shape ``com.amazonaws.greengrass#DeleteSubscriptionDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class DeleteSubscriptionDefinitionRequest(TypedDict):
    subscription_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the subscription definition."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriptionDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSubscriptionDefinitionRequest:
    out: DeleteSubscriptionDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
