"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftProvisionedConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.redshift_cluster_identifier
    import aws_sdk_bedrock_agent.types.redshift_provisioned_auth_configuration


class RedshiftProvisionedConfiguration(TypedDict):
    cluster_identifier: "aws_sdk_bedrock_agent.types.redshift_cluster_identifier.RedshiftClusterIdentifier"
    """<p>The ID of the Amazon Redshift cluster.</p>"""
    auth_configuration: "aws_sdk_bedrock_agent.types.redshift_provisioned_auth_configuration.RedshiftProvisionedAuthConfiguration"
    """<p>Specifies configurations for authentication to Amazon Redshift.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftProvisionedConfiguration) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    import aws_sdk_bedrock_agent.types.redshift_provisioned_auth_configuration

    out["authConfiguration"] = (
        aws_sdk_bedrock_agent.types.redshift_provisioned_auth_configuration.serialize_json(
            value["auth_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RedshiftProvisionedConfiguration:
    out: RedshiftProvisionedConfiguration = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError(
            "RedshiftProvisionedConfiguration.cluster_identifier required"
        )
    if "authConfiguration" in data:
        import aws_sdk_bedrock_agent.types.redshift_provisioned_auth_configuration

        out["auth_configuration"] = (
            aws_sdk_bedrock_agent.types.redshift_provisioned_auth_configuration.deserialize_json(
                data["authConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftProvisionedConfiguration.auth_configuration required"
        )
    return out
