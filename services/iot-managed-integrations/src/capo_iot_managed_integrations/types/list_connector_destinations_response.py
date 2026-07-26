"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListConnectorDestinationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.connector_destination_list_definition
    import capo_iot_managed_integrations.types.next_token


class ListConnectorDestinationsResponse(TypedDict, closed=True):
    connector_destination_list: NotRequired[
        "capo_iot_managed_integrations.types.connector_destination_list_definition.ConnectorDestinationListDefinition"
    ]
    """<p>The list of connector destinations that match the specified criteria.</p>"""
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token used for pagination of results when there are more connector destinations than can be returned in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorDestinationsResponse) -> dict:
    out: dict = {}
    if "connector_destination_list" in value:
        import capo_iot_managed_integrations.types.connector_destination_list_definition

        out["ConnectorDestinationList"] = (
            capo_iot_managed_integrations.types.connector_destination_list_definition.serialize_json(
                value["connector_destination_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorDestinationsResponse:
    out: ListConnectorDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "ConnectorDestinationList" in data:
        import capo_iot_managed_integrations.types.connector_destination_list_definition

        out["connector_destination_list"] = (
            capo_iot_managed_integrations.types.connector_destination_list_definition.deserialize_json(
                data["ConnectorDestinationList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
