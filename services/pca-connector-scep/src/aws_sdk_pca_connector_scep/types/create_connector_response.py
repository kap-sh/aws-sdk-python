"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#CreateConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.connector_arn


class CreateConnectorResponse(TypedDict):
    connector_arn: NotRequired[
        "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn"
    ]
    """<p>Returns the Amazon Resource Name (ARN) of the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    return out


def deserialize_json(data: dict) -> CreateConnectorResponse:
    out: CreateConnectorResponse = {}  # type: ignore[typeddict-item]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    return out
