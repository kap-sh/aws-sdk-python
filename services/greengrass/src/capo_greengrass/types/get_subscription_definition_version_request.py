"""Generated from Smithy shape ``com.amazonaws.greengrass#GetSubscriptionDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class GetSubscriptionDefinitionVersionRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""
    subscription_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the subscription definition."""
    subscription_definition_version_id: "capo_greengrass.types.__string.__string"
    """The ID of the subscription definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListSubscriptionDefinitionVersions'' requests. If the version is the last one that was associated with a subscription definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object."""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionDefinitionVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSubscriptionDefinitionVersionRequest:
    out: GetSubscriptionDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    return out
