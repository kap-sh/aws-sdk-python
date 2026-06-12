"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftServerlessConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.redshift_serverless_auth_configuration
    import aws_sdk_bedrock_agent.types.workgroup_arn


class RedshiftServerlessConfiguration(TypedDict):
    workgroup_arn: "aws_sdk_bedrock_agent.types.workgroup_arn.WorkgroupArn"
    """<p>The ARN of the Amazon Redshift workgroup.</p>"""
    auth_configuration: "aws_sdk_bedrock_agent.types.redshift_serverless_auth_configuration.RedshiftServerlessAuthConfiguration"
    """<p>Specifies configurations for authentication to an Amazon Redshift provisioned data warehouse.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftServerlessConfiguration) -> dict:
    out: dict = {}
    out["workgroupArn"] = value["workgroup_arn"]
    import aws_sdk_bedrock_agent.types.redshift_serverless_auth_configuration

    out["authConfiguration"] = (
        aws_sdk_bedrock_agent.types.redshift_serverless_auth_configuration.serialize_json(
            value["auth_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RedshiftServerlessConfiguration:
    out: RedshiftServerlessConfiguration = {}  # type: ignore[typeddict-item]
    if "workgroupArn" in data:
        out["workgroup_arn"] = data["workgroupArn"]
    else:
        raise DeserializationError(
            "RedshiftServerlessConfiguration.workgroup_arn required"
        )
    if "authConfiguration" in data:
        import aws_sdk_bedrock_agent.types.redshift_serverless_auth_configuration

        out["auth_configuration"] = (
            aws_sdk_bedrock_agent.types.redshift_serverless_auth_configuration.deserialize_json(
                data["authConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftServerlessConfiguration.auth_configuration required"
        )
    return out
