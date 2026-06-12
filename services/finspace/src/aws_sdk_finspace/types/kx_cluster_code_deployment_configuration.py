"""Generated from Smithy shape ``com.amazonaws.finspace#KxClusterCodeDeploymentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_cluster_code_deployment_strategy


class KxClusterCodeDeploymentConfiguration(TypedDict):
    deployment_strategy: "aws_sdk_finspace.types.kx_cluster_code_deployment_strategy.KxClusterCodeDeploymentStrategy"
    """<p> The type of deployment that you want on a cluster. </p> <ul> <li> <p>ROLLING – This options updates the cluster by stopping the exiting q process and starting a new q process with updated configuration.</p> </li> <li> <p>NO_RESTART – This option updates the cluster without stopping the running q process. It is only available for <code>GP</code> type cluster. This option is quicker as it reduces the turn around time to update configuration on a cluster. </p> <p>With this deployment mode, you cannot update the <code>initializationScript</code> and <code>commandLineArguments</code> parameters.</p> </li> <li> <p>FORCE – This option updates the cluster by immediately stopping all the running processes before starting up new ones with the updated configuration. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxClusterCodeDeploymentConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_finspace.types.kx_cluster_code_deployment_strategy

    out["deploymentStrategy"] = (
        aws_sdk_finspace.types.kx_cluster_code_deployment_strategy.serialize_json(
            value["deployment_strategy"]
        )
    )
    return out


def deserialize_json(data: dict) -> KxClusterCodeDeploymentConfiguration:
    out: KxClusterCodeDeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if "deploymentStrategy" in data:
        import aws_sdk_finspace.types.kx_cluster_code_deployment_strategy

        out["deployment_strategy"] = (
            aws_sdk_finspace.types.kx_cluster_code_deployment_strategy.deserialize_json(
                data["deploymentStrategy"]
            )
        )
    else:
        raise DeserializationError(
            "KxClusterCodeDeploymentConfiguration.deployment_strategy required"
        )
    return out
