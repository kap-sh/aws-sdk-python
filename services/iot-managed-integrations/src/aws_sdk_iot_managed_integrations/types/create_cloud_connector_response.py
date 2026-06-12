"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateCloudConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.cloud_connector_id


class CreateCloudConnectorResponse(TypedDict):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    ]
    """<p>The unique identifier assigned to the newly created cloud connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCloudConnectorResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateCloudConnectorResponse:
    out: CreateCloudConnectorResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
