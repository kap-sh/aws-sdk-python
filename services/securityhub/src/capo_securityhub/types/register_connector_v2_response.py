"""Generated from Smithy shape ``com.amazonaws.securityhub#RegisterConnectorV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class RegisterConnectorV2Response(TypedDict, closed=True):
    connector_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the connectorV2.</p>"""
    connector_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The UUID of the connectorV2 to identify connectorV2 resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterConnectorV2Response) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    return out


def deserialize_json(data: dict) -> RegisterConnectorV2Response:
    out: RegisterConnectorV2Response = {}  # type: ignore[typeddict-item]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    return out
