"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateConnectorDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.connector_destination_id


class CreateConnectorDestinationResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>The identifier of the C2C connector destination creation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorDestinationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateConnectorDestinationResponse:
    out: CreateConnectorDestinationResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
