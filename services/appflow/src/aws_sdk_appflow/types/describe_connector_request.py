"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_label
    import aws_sdk_appflow.types.connector_type


class DescribeConnectorRequest(TypedDict):
    connector_type: "aws_sdk_appflow.types.connector_type.ConnectorType"
    """<p>The connector type, such as CUSTOMCONNECTOR, Saleforce, Marketo. Please choose CUSTOMCONNECTOR for Lambda based custom connectors.</p>"""
    connector_label: NotRequired["aws_sdk_appflow.types.connector_label.ConnectorLabel"]
    """<p>The label of the connector. The label is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorRequest) -> dict:
    out: dict = {}
    import aws_sdk_appflow.types.connector_type

    out["connectorType"] = aws_sdk_appflow.types.connector_type.serialize_json(
        value["connector_type"]
    )
    if "connector_label" in value:
        out["connectorLabel"] = value["connector_label"]
    return out


def deserialize_json(data: dict) -> DescribeConnectorRequest:
    out: DescribeConnectorRequest = {}  # type: ignore[typeddict-item]
    if "connectorType" in data:
        import aws_sdk_appflow.types.connector_type

        out["connector_type"] = aws_sdk_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    else:
        raise DeserializationError("DescribeConnectorRequest.connector_type required")
    if "connectorLabel" in data:
        out["connector_label"] = data["connectorLabel"]
    return out
