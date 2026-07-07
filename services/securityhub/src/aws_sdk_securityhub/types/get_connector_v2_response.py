"""Generated from Smithy shape ``com.amazonaws.securityhub#GetConnectorV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.health_check
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.provider_detail
    import aws_sdk_securityhub.types.timestamp


class GetConnectorV2Response(TypedDict, closed=True):
    connector_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the connectorV2.</p>"""
    connector_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The UUID of the connectorV2 to identify connectorV2 resource.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the connectorV2.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the connectorV2.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of KMS key used for the connectorV2.</p>"""
    created_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>ISO 8601 UTC timestamp for the time create the connectorV2.</p>"""
    last_updated_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>ISO 8601 UTC timestamp for the time update the connectorV2 connectorStatus.</p>"""
    health: NotRequired["aws_sdk_securityhub.types.health_check.HealthCheck"]
    """<p>The current health status for connectorV2</p>"""
    provider_detail: NotRequired[
        "aws_sdk_securityhub.types.provider_detail.ProviderDetail"
    ]
    """<p>The third-party provider detail for a service configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorV2Response) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "created_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["CreatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "health" in value:
        import aws_sdk_securityhub.types.health_check

        out["Health"] = aws_sdk_securityhub.types.health_check.serialize_json(
            value["health"]
        )
    if "provider_detail" in value:
        import aws_sdk_securityhub.types.provider_detail

        out["ProviderDetail"] = (
            aws_sdk_securityhub.types.provider_detail.serialize_json(
                value["provider_detail"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConnectorV2Response:
    out: GetConnectorV2Response = {}  # type: ignore[typeddict-item]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "CreatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["created_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["last_updated_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["LastUpdatedAt"]
        )
    if "Health" in data:
        import aws_sdk_securityhub.types.health_check

        out["health"] = aws_sdk_securityhub.types.health_check.deserialize_json(
            data["Health"]
        )
    if "ProviderDetail" in data:
        import aws_sdk_securityhub.types.provider_detail

        out["provider_detail"] = (
            aws_sdk_securityhub.types.provider_detail.deserialize_json(
                data["ProviderDetail"]
            )
        )
    return out
