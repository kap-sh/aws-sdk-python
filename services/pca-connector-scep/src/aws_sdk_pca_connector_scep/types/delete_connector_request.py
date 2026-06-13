"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#DeleteConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.connector_arn


class DeleteConnectorRequest(TypedDict):
    connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the connector to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectorRequest:
    out: DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
