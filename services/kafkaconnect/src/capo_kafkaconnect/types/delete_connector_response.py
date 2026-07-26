"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DeleteConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.connector_state


class DeleteConnectorResponse(TypedDict, closed=True):
    connector_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector that you requested to delete.</p>"""
    connector_state: NotRequired[
        "capo_kafkaconnect.types.connector_state.ConnectorState"
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
