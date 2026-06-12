"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.connector_id


class DeleteConnectorRequest(TypedDict):
    connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId"
    """<p>The unique identifier for the connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectorRequest) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectorRequest:
    out: DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    else:
        raise DeserializationError("DeleteConnectorRequest.connector_id required")
    return out
