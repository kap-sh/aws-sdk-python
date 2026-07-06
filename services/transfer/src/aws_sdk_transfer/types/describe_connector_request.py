"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.connector_id


class DescribeConnectorRequest(TypedDict, closed=True):
    connector_id: "aws_sdk_transfer.types.connector_id.ConnectorId"
    """<p>The unique identifier for the connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectorRequest) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectorRequest:
    out: DescribeConnectorRequest = {}  # type: ignore[typeddict-item]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    else:
        raise DeserializationError("DescribeConnectorRequest.connector_id required")
    return out
