"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteConnectorDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.connector_destination_id


class DeleteConnectorDestinationRequest(TypedDict, closed=True):
    identifier: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    """<p>The identifier of the connector destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectorDestinationRequest:
    out: DeleteConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
