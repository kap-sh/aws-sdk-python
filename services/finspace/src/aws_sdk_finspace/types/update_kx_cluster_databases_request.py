"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxClusterDatabasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token_string
    import aws_sdk_finspace.types.kx_cluster_name
    import aws_sdk_finspace.types.kx_database_configurations
    import aws_sdk_finspace.types.kx_deployment_configuration
    import aws_sdk_finspace.types.kx_environment_id


class UpdateKxClusterDatabasesRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>The unique identifier of a kdb environment.</p>"""
    cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName"
    """<p>A unique name for the cluster that you want to modify.</p>"""
    client_token: NotRequired[
        "aws_sdk_finspace.types.client_token_string.ClientTokenString"
    ]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    databases: (
        "aws_sdk_finspace.types.kx_database_configurations.KxDatabaseConfigurations"
    )
    """<p> The structure of databases mounted on the cluster.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_finspace.types.kx_deployment_configuration.KxDeploymentConfiguration"
    ]
    """<p> The configuration that allows you to choose how you want to update the databases on a cluster. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxClusterDatabasesRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_finspace.types.kx_database_configurations

    out["databases"] = aws_sdk_finspace.types.kx_database_configurations.serialize_json(
        value["databases"]
    )
    if "deployment_configuration" in value:
        import aws_sdk_finspace.types.kx_deployment_configuration

        out["deploymentConfiguration"] = (
            aws_sdk_finspace.types.kx_deployment_configuration.serialize_json(
                value["deployment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKxClusterDatabasesRequest:
    out: UpdateKxClusterDatabasesRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "databases" in data:
        import aws_sdk_finspace.types.kx_database_configurations

        out["databases"] = (
            aws_sdk_finspace.types.kx_database_configurations.deserialize_json(
                data["databases"]
            )
        )
    else:
        raise DeserializationError("UpdateKxClusterDatabasesRequest.databases required")
    if "deploymentConfiguration" in data:
        import aws_sdk_finspace.types.kx_deployment_configuration

        out["deployment_configuration"] = (
            aws_sdk_finspace.types.kx_deployment_configuration.deserialize_json(
                data["deploymentConfiguration"]
            )
        )
    return out
