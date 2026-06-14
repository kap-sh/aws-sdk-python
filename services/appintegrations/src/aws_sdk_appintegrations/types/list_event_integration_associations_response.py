"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListEventIntegrationAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.event_integration_associations_list
    import aws_sdk_appintegrations.types.next_token


class ListEventIntegrationAssociationsResponse(TypedDict):
    event_integration_associations: NotRequired[
        "aws_sdk_appintegrations.types.event_integration_associations_list.EventIntegrationAssociationsList"
    ]
    """<p>The event integration associations.</p>"""
    next_token: NotRequired["aws_sdk_appintegrations.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventIntegrationAssociationsResponse) -> dict:
    out: dict = {}
    if "event_integration_associations" in value:
        import aws_sdk_appintegrations.types.event_integration_associations_list

        out["EventIntegrationAssociations"] = (
            aws_sdk_appintegrations.types.event_integration_associations_list.serialize_json(
                value["event_integration_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventIntegrationAssociationsResponse:
    out: ListEventIntegrationAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "EventIntegrationAssociations" in data:
        import aws_sdk_appintegrations.types.event_integration_associations_list

        out["event_integration_associations"] = (
            aws_sdk_appintegrations.types.event_integration_associations_list.deserialize_json(
                data["EventIntegrationAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
