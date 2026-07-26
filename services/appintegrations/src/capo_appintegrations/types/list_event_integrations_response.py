"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListEventIntegrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.event_integrations_list
    import capo_appintegrations.types.next_token


class ListEventIntegrationsResponse(TypedDict, closed=True):
    event_integrations: NotRequired[
        "capo_appintegrations.types.event_integrations_list.EventIntegrationsList"
    ]
    """<p>The event integrations.</p>"""
    next_token: NotRequired["capo_appintegrations.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventIntegrationsResponse) -> dict:
    out: dict = {}
    if "event_integrations" in value:
        import capo_appintegrations.types.event_integrations_list

        out["EventIntegrations"] = (
            capo_appintegrations.types.event_integrations_list.serialize_json(
                value["event_integrations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventIntegrationsResponse:
    out: ListEventIntegrationsResponse = {}  # type: ignore[typeddict-item]
    if "EventIntegrations" in data:
        import capo_appintegrations.types.event_integrations_list

        out["event_integrations"] = (
            capo_appintegrations.types.event_integrations_list.deserialize_json(
                data["EventIntegrations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
