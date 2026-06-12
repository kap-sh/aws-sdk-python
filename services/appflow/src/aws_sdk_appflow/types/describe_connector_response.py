"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_configuration


class DescribeConnectorResponse(TypedDict):
    connector_configuration: NotRequired[
        "aws_sdk_appflow.types.connector_configuration.ConnectorConfiguration"
    ]
    """<p>Configuration info of all the connectors that the user requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorResponse) -> dict:
    out: dict = {}
    if "connector_configuration" in value:
        import aws_sdk_appflow.types.connector_configuration

        out["connectorConfiguration"] = (
            aws_sdk_appflow.types.connector_configuration.serialize_json(
                value["connector_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeConnectorResponse:
    out: DescribeConnectorResponse = {}  # type: ignore[typeddict-item]
    if "connectorConfiguration" in data:
        import aws_sdk_appflow.types.connector_configuration

        out["connector_configuration"] = (
            aws_sdk_appflow.types.connector_configuration.deserialize_json(
                data["connectorConfiguration"]
            )
        )
    return out
