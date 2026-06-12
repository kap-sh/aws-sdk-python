"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DeleteConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.connector_state


class DeleteConnectorResponse(TypedDict):
    connector_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector that you requested to delete.</p>"""
    connector_state: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_state.ConnectorState"
    ]
    """<p>The state of the connector that you requested to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    if "connector_state" in value:
        out["connectorState"] = value["connector_state"]
    return out


def deserialize_json(data: dict) -> DeleteConnectorResponse:
    out: DeleteConnectorResponse = {}  # type: ignore[typeddict-item]
    if "connectorArn" in data:
        out["connector_arn"] = data["connectorArn"]
    if "connectorState" in data:
        out["connector_state"] = data["connectorState"]
    return out
