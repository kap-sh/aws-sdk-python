"""Generated from Smithy shape ``com.amazonaws.bedrock#MarketplaceModelEndpointSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.arn
    import aws_sdk_bedrock.types.model_source_identifier
    import aws_sdk_bedrock.types.status
    import aws_sdk_bedrock.types.timestamp


class MarketplaceModelEndpointSummary(TypedDict, closed=True):
    endpoint_arn: "aws_sdk_bedrock.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    model_source_identifier: (
        "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier"
    )
    """<p>The ARN of the model from Amazon Bedrock Marketplace that is deployed on this endpoint.</p>"""
    status: NotRequired["aws_sdk_bedrock.types.status.Status"]
    """<p>The overall status of the endpoint in Amazon Bedrock Marketplace.</p>"""
    status_message: NotRequired["str"]
    """<p>Additional information about the overall status, if available.</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the endpoint was created.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the endpoint was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarketplaceModelEndpointSummary) -> dict:
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
    return out


def deserialize_json(data: dict) -> MarketplaceModelEndpointSummary:
    out: MarketplaceModelEndpointSummary = {}  # type: ignore[typeddict-item]
    if "endpointArn" in data:
        out["endpoint_arn"] = data["endpointArn"]
    else:
        raise DeserializationError(
            "MarketplaceModelEndpointSummary.endpoint_arn required"
        )
    if "modelSourceIdentifier" in data:
        out["model_source_identifier"] = data["modelSourceIdentifier"]
    else:
        raise DeserializationError(
            "MarketplaceModelEndpointSummary.model_source_identifier required"
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
        raise DeserializationError(
            "MarketplaceModelEndpointSummary.created_at required"
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "MarketplaceModelEndpointSummary.updated_at required"
        )
    return out
