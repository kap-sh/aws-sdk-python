"""Generated from Smithy shape ``com.amazonaws.eks#ConnectorConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.connector_config_provider
    import aws_sdk_eks.types.string


class ConnectorConfigRequest(TypedDict, closed=True):
    role_arn: "aws_sdk_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the role that is authorized to request the connector configuration.</p>"""
    provider: "aws_sdk_eks.types.connector_config_provider.ConnectorConfigProvider"
    """<p>The cloud provider for the target cluster to connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorConfigRequest) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    import aws_sdk_eks.types.connector_config_provider

    out["provider"] = aws_sdk_eks.types.connector_config_provider.serialize_json(
        value["provider"]
    )
    return out


def deserialize_json(data: dict) -> ConnectorConfigRequest:
    out: ConnectorConfigRequest = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ConnectorConfigRequest.role_arn required")
    if "provider" in data:
        import aws_sdk_eks.types.connector_config_provider

        out["provider"] = aws_sdk_eks.types.connector_config_provider.deserialize_json(
            data["provider"]
        )
    else:
        raise DeserializationError("ConnectorConfigRequest.provider required")
    return out
