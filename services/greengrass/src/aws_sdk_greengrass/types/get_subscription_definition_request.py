"""Generated from Smithy shape ``com.amazonaws.greengrass#GetSubscriptionDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetSubscriptionDefinitionRequest(TypedDict, closed=True):
    subscription_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the subscription definition."""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSubscriptionDefinitionRequest:
    out: GetSubscriptionDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
