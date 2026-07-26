"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.connector_configurations_map
    import capo_appflow.types.connector_list
    import capo_appflow.types.next_token


class DescribeConnectorsResponse(TypedDict, closed=True):
    connector_configurations: NotRequired[
        "capo_appflow.types.connector_configurations_map.ConnectorConfigurationsMap"
    ]
    """<p> The configuration that is applied to the connectors used in the flow. </p>"""
    connectors: NotRequired["capo_appflow.types.connector_list.ConnectorList"]
    """<p>Information about the connectors supported in Amazon AppFlow.</p>"""
    next_token: NotRequired["capo_appflow.types.next_token.NextToken"]
    """<p> The pagination token for the next page of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorsResponse) -> dict:
    out: dict = {}
    if "connector_configurations" in value:
        import capo_appflow.types.connector_configurations_map

        out["connectorConfigurations"] = (
            capo_appflow.types.connector_configurations_map.serialize_json(
                value["connector_configurations"]
            )
        )
    if "connectors" in value:
        import capo_appflow.types.connector_list

        out["connectors"] = capo_appflow.types.connector_list.serialize_json(
            value["connectors"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeConnectorsResponse:
    out: DescribeConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "connectorConfigurations" in data:
        import capo_appflow.types.connector_configurations_map

        out["connector_configurations"] = (
            capo_appflow.types.connector_configurations_map.deserialize_json(
                data["connectorConfigurations"]
            )
        )
    if "connectors" in data:
        import capo_appflow.types.connector_list

        out["connectors"] = capo_appflow.types.connector_list.deserialize_json(
            data["connectors"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
