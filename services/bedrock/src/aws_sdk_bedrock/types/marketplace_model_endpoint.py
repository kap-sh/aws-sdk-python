"""Generated from Smithy shape ``com.amazonaws.bedrock#MarketplaceModelEndpoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.arn
    import aws_sdk_bedrock.types.endpoint_config
    import aws_sdk_bedrock.types.model_source_identifier
    import aws_sdk_bedrock.types.status
    import aws_sdk_bedrock.types.timestamp


class MarketplaceModelEndpoint(TypedDict):
    endpoint_arn: "aws_sdk_bedrock.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    model_source_identifier: (
        "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier"
    )
    """<p>The ARN of the model from Amazon Bedrock Marketplace that is deployed on this endpoint.</p>"""
    status: NotRequired["aws_sdk_bedrock.types.status.Status"]
    """<p>The overall status of the endpoint in Amazon Bedrock Marketplace (e.g., ACTIVE, INACTIVE).</p>"""
    status_message: NotRequired["str"]
    """<p>Additional information about the overall status, if available.</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the endpoint was registered.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the endpoint was last updated.</p>"""
    endpoint_config: "aws_sdk_bedrock.types.endpoint_config.EndpointConfig"
    """<p>The configuration of the endpoint, including the number and type of instances used.</p>"""
    endpoint_status: "str"
    """<p>The current status of the endpoint (e.g., Creating, InService, Updating, Failed).</p>"""
    endpoint_status_message: NotRequired["str"]
    """<p>Additional information about the endpoint status, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarketplaceModelEndpoint) -> dict:
    out: dict = {}
    out["endpointArn"] = value["endpoint_arn"]
    out["modelSourceIdentifier"] = value["model_source_identifier"]
    if "status" in value:
        import aws_sdk_bedrock.types.status

        out["status"] = aws_sdk_bedrock.types.status.serialize_json(value["status"])
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    import aws_sdk_bedrock.types.endpoint_config

    out["endpointConfig"] = aws_sdk_bedrock.types.endpoint_config.serialize_json(
        value["endpoint_config"]
    )
    out["endpointStatus"] = value["endpoint_status"]
    if "endpoint_status_message" in value:
        out["endpointStatusMessage"] = value["endpoint_status_message"]
    return out


def deserialize_json(data: dict) -> MarketplaceModelEndpoint:
    out: MarketplaceModelEndpoint = {}  # type: ignore[typeddict-item]
    if "endpointArn" in data:
        out["endpoint_arn"] = data["endpointArn"]
    else:
        raise DeserializationError("MarketplaceModelEndpoint.endpoint_arn required")
    if "modelSourceIdentifier" in data:
        out["model_source_identifier"] = data["modelSourceIdentifier"]
    else:
        raise DeserializationError(
            "MarketplaceModelEndpoint.model_source_identifier required"
        )
    if "status" in data:
        import aws_sdk_bedrock.types.status

        out["status"] = aws_sdk_bedrock.types.status.deserialize_json(data["status"])
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("MarketplaceModelEndpoint.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("MarketplaceModelEndpoint.updated_at required")
    if "endpointConfig" in data:
        import aws_sdk_bedrock.types.endpoint_config

        out["endpoint_config"] = aws_sdk_bedrock.types.endpoint_config.deserialize_json(
            data["endpointConfig"]
        )
    else:
        raise DeserializationError("MarketplaceModelEndpoint.endpoint_config required")
    if "endpointStatus" in data:
        out["endpoint_status"] = data["endpointStatus"]
    else:
        raise DeserializationError("MarketplaceModelEndpoint.endpoint_status required")
    if "endpointStatusMessage" in data:
        out["endpoint_status_message"] = data["endpointStatusMessage"]
    return out
