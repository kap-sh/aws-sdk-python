"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateSubscriptionDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class UpdateSubscriptionDefinitionRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The name of the definition."""
    subscription_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the subscription definition."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriptionDefinitionRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateSubscriptionDefinitionRequest:
    out: UpdateSubscriptionDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
