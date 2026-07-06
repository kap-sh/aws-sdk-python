"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateConnectorV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.connector_status
    import aws_sdk_securityhub.types.non_empty_string


class CreateConnectorV2Response(TypedDict, closed=True):
    connector_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the connectorV2.</p>"""
    connector_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The UUID of the connectorV2 to identify connectorV2 resource.</p>"""
    auth_url: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Url provide to customers for OAuth auth code flow.</p>"""
    connector_status: NotRequired[
        "aws_sdk_securityhub.types.connector_status.ConnectorStatus"
    ]
    """<p>The current status of the connectorV2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorV2Response) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    if "auth_url" in value:
        out["AuthUrl"] = value["auth_url"]
    if "connector_status" in value:
        import aws_sdk_securityhub.types.connector_status

        out["ConnectorStatus"] = (
            aws_sdk_securityhub.types.connector_status.serialize_json(
                value["connector_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateConnectorV2Response:
    out: CreateConnectorV2Response = {}  # type: ignore[typeddict-item]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    if "AuthUrl" in data:
        out["auth_url"] = data["AuthUrl"]
    if "ConnectorStatus" in data:
        import aws_sdk_securityhub.types.connector_status

        out["connector_status"] = (
            aws_sdk_securityhub.types.connector_status.deserialize_json(
                data["ConnectorStatus"]
            )
        )
    return out
