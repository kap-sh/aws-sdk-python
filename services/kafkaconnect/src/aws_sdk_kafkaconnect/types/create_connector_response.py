"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CreateConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.connector_state


class CreateConnectorResponse(TypedDict, closed=True):
    connector_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that Amazon assigned to the connector.</p>"""
    connector_name: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The name of the connector.</p>"""
    connector_state: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_state.ConnectorState"
    ]
    """<p>The state of the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    if "connector_name" in value:
        out["connectorName"] = value["connector_name"]
    if "connector_state" in value:
        out["connectorState"] = value["connector_state"]
    return out


def deserialize_json(data: dict) -> CreateConnectorResponse:
    out: CreateConnectorResponse = {}  # type: ignore[typeddict-item]
    if "connectorArn" in data:
        out["connector_arn"] = data["connectorArn"]
    if "connectorName" in data:
        out["connector_name"] = data["connectorName"]
    if "connectorState" in data:
        out["connector_state"] = data["connectorState"]
    return out
