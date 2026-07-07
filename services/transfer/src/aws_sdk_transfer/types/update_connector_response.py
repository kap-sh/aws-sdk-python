"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.connector_id


class UpdateConnectorResponse(TypedDict, closed=True):
    connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId"
    """<p>Returns the identifier of the connector object that you are updating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectorResponse) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectorResponse:
    out: UpdateConnectorResponse = {}  # type: ignore[typeddict-item]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    else:
        raise DeserializationError("UpdateConnectorResponse.connector_id required")
    return out
