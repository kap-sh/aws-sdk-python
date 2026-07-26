"""Generated from Smithy shape ``com.amazonaws.greengrass#DeleteSubscriptionDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class DeleteSubscriptionDefinitionRequest(TypedDict, closed=True):
    subscription_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the subscription definition."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriptionDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSubscriptionDefinitionRequest:
    out: DeleteSubscriptionDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
