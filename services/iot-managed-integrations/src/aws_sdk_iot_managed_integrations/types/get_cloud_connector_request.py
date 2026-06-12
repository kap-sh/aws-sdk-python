"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetCloudConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.cloud_connector_id


class GetCloudConnectorRequest(TypedDict):
    identifier: (
        "aws_sdk_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    )
    """<p>The identifier of the C2C connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCloudConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCloudConnectorRequest:
    out: GetCloudConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
