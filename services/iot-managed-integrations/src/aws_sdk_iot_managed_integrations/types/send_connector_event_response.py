"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SendConnectorEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.connector_id


class SendConnectorEventResponse(TypedDict, closed=True):
    connector_id: "aws_sdk_iot_managed_integrations.types.connector_id.ConnectorId"
    """<p>The id of the connector between the third-party cloud provider and IoT managed integrations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendConnectorEventResponse) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    return out


def deserialize_json(data: dict) -> SendConnectorEventResponse:
    out: SendConnectorEventResponse = {}  # type: ignore[typeddict-item]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    else:
        raise DeserializationError("SendConnectorEventResponse.connector_id required")
    return out
