"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiKeyCredentialProviderItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.api_key_credential_provider_arn_type
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name


class ApiKeyCredentialProviderItem(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the API key credential provider.</p>"""
    credential_provider_arn: "aws_sdk_bedrock_agentcore_control.types.api_key_credential_provider_arn_type.ApiKeyCredentialProviderArnType"
    """<p>The Amazon Resource Name (ARN) of the API key credential provider.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the API key credential provider was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The timestamp when the API key credential provider was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyCredentialProviderItem) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["credentialProviderArn"] = value["credential_provider_arn"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["createdTime"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["lastUpdatedTime"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApiKeyCredentialProviderItem:
    out: ApiKeyCredentialProviderItem = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ApiKeyCredentialProviderItem.name required")
    if "credentialProviderArn" in data:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        raise DeserializationError(
            "ApiKeyCredentialProviderItem.credential_provider_arn required"
        )
    if "createdTime" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("ApiKeyCredentialProviderItem.created_time required")
    if "lastUpdatedTime" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["last_updated_time"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError(
            "ApiKeyCredentialProviderItem.last_updated_time required"
        )
    return out
