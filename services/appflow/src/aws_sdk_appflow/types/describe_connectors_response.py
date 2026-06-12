"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_configurations_map
    import aws_sdk_appflow.types.connector_list
    import aws_sdk_appflow.types.next_token


class DescribeConnectorsResponse(TypedDict):
    connector_configurations: NotRequired[
        "aws_sdk_appflow.types.connector_configurations_map.ConnectorConfigurationsMap"
    ]
    """<p> The configuration that is applied to the connectors used in the flow. </p>"""
    connectors: NotRequired["aws_sdk_appflow.types.connector_list.ConnectorList"]
    """<p>Information about the connectors supported in Amazon AppFlow.</p>"""
    next_token: NotRequired["aws_sdk_appflow.types.next_token.NextToken"]
    """<p> The pagination token for the next page of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorsResponse) -> dict:
    out: dict = {}
    if "connector_configurations" in value:
        import aws_sdk_appflow.types.connector_configurations_map

        out["connectorConfigurations"] = (
            aws_sdk_appflow.types.connector_configurations_map.serialize_json(
                value["connector_configurations"]
            )
        )
    if "connectors" in value:
        import aws_sdk_appflow.types.connector_list

        out["connectors"] = aws_sdk_appflow.types.connector_list.serialize_json(
            value["connectors"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeConnectorsResponse:
    out: DescribeConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "connectorConfigurations" in data:
        import aws_sdk_appflow.types.connector_configurations_map

        out["connector_configurations"] = (
            aws_sdk_appflow.types.connector_configurations_map.deserialize_json(
                data["connectorConfigurations"]
            )
        )
    if "connectors" in data:
        import aws_sdk_appflow.types.connector_list

        out["connectors"] = aws_sdk_appflow.types.connector_list.deserialize_json(
            data["connectors"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
