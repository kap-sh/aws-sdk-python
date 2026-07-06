"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CreateConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.connector_arn


class CreateConnectorResponse(TypedDict, closed=True):
    connector_arn: NotRequired[
        "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn"
    ]
    """<p>If successful, the Amazon Resource Name (ARN) of the connector for Active Directory.</p>"""


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
