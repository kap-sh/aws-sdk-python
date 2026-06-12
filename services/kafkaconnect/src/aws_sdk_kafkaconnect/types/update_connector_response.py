"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#UpdateConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.connector_state


class UpdateConnectorResponse(TypedDict):
    connector_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    connector_state: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_state.ConnectorState"
    ]
    """<p>The state of the connector.</p>"""
    connector_operation_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    if "connector_state" in value:
        out["connectorState"] = value["connector_state"]
    if "connector_operation_arn" in value:
        out["connectorOperationArn"] = value["connector_operation_arn"]
    return out


def deserialize_json(data: dict) -> UpdateConnectorResponse:
    out: UpdateConnectorResponse = {}  # type: ignore[typeddict-item]
    if "connectorArn" in data:
        out["connector_arn"] = data["connectorArn"]
    if "connectorState" in data:
        out["connector_state"] = data["connectorState"]
    if "connectorOperationArn" in data:
        out["connector_operation_arn"] = data["connectorOperationArn"]
    return out
