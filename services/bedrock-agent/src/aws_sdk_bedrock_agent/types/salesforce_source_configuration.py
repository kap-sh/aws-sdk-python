"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SalesforceSourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.https_url
    import aws_sdk_bedrock_agent.types.salesforce_auth_type
    import aws_sdk_bedrock_agent.types.secret_arn


class SalesforceSourceConfiguration(TypedDict):
    host_url: "aws_sdk_bedrock_agent.types.https_url.HttpsUrl"
    """<p>The Salesforce host URL or instance URL.</p>"""
    auth_type: "aws_sdk_bedrock_agent.types.salesforce_auth_type.SalesforceAuthType"
    """<p>The supported authentication type to authenticate and connect to your Salesforce instance.</p>"""
    credentials_secret_arn: "aws_sdk_bedrock_agent.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name of an Secrets Manager secret that stores your authentication credentials for your Salesforce instance URL. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/salesforce-data-source-connector.html#configuration-salesforce-connector\">Salesforce connection configuration</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceSourceConfiguration) -> dict:
    out: dict = {}
    out["hostUrl"] = value["host_url"]
    import aws_sdk_bedrock_agent.types.salesforce_auth_type

    out["authType"] = aws_sdk_bedrock_agent.types.salesforce_auth_type.serialize_json(
        value["auth_type"]
    )
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    return out


def deserialize_json(data: dict) -> SalesforceSourceConfiguration:
    out: SalesforceSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "hostUrl" in data:
        out["host_url"] = data["hostUrl"]
    else:
        raise DeserializationError("SalesforceSourceConfiguration.host_url required")
    if "authType" in data:
        import aws_sdk_bedrock_agent.types.salesforce_auth_type

        out["auth_type"] = (
            aws_sdk_bedrock_agent.types.salesforce_auth_type.deserialize_json(
                data["authType"]
            )
        )
    else:
        raise DeserializationError("SalesforceSourceConfiguration.auth_type required")
    if "credentialsSecretArn" in data:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        raise DeserializationError(
            "SalesforceSourceConfiguration.credentials_secret_arn required"
        )
    return out
