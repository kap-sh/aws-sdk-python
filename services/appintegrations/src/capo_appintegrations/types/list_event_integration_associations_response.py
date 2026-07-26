"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListEventIntegrationAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.event_integration_associations_list
    import capo_appintegrations.types.next_token


class ListEventIntegrationAssociationsResponse(TypedDict, closed=True):
    event_integration_associations: NotRequired[
        "capo_appintegrations.types.event_integration_associations_list.EventIntegrationAssociationsList"
    ]
    """<p>The event integration associations.</p>"""
    next_token: NotRequired["capo_appintegrations.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventIntegrationAssociationsResponse) -> dict:
    out: dict = {}
    if "event_integration_associations" in value:
        import capo_appintegrations.types.event_integration_associations_list

        out["EventIntegrationAssociations"] = (
            capo_appintegrations.types.event_integration_associations_list.serialize_json(
                value["event_integration_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventIntegrationAssociationsResponse:
    out: ListEventIntegrationAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "EventIntegrationAssociations" in data:
        import capo_appintegrations.types.event_integration_associations_list

        out["event_integration_associations"] = (
            capo_appintegrations.types.event_integration_associations_list.deserialize_json(
                data["EventIntegrationAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
