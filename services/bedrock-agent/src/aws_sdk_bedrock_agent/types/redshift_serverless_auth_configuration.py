"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftServerlessAuthConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.redshift_serverless_auth_type
    import aws_sdk_bedrock_agent.types.secret_arn


class RedshiftServerlessAuthConfiguration(TypedDict):
    type: "aws_sdk_bedrock_agent.types.redshift_serverless_auth_type.RedshiftServerlessAuthType"
    """<p>The type of authentication to use.</p>"""
    username_password_secret_arn: NotRequired[
        "aws_sdk_bedrock_agent.types.secret_arn.SecretArn"
    ]
    """<p>The ARN of an Secrets Manager secret for authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftServerlessAuthConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.redshift_serverless_auth_type

    out["type"] = (
        aws_sdk_bedrock_agent.types.redshift_serverless_auth_type.serialize_json(
            value["type"]
        )
    )
    if "username_password_secret_arn" in value:
        out["usernamePasswordSecretArn"] = value["username_password_secret_arn"]
    return out


def deserialize_json(data: dict) -> RedshiftServerlessAuthConfiguration:
    out: RedshiftServerlessAuthConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.redshift_serverless_auth_type

        out["type"] = (
            aws_sdk_bedrock_agent.types.redshift_serverless_auth_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("RedshiftServerlessAuthConfiguration.type required")
    if "usernamePasswordSecretArn" in data:
        out["username_password_secret_arn"] = data["usernamePasswordSecretArn"]
    return out
