"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.sb_client_token
    import capo_pcs.types.update_cluster_slurm_configuration_request


class UpdateClusterRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster to update.</p>"""
    client_token: NotRequired["capo_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>"""
    slurm_configuration: NotRequired[
        "capo_pcs.types.update_cluster_slurm_configuration_request.UpdateClusterSlurmConfigurationRequest"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateClusterRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "slurm_configuration" in value:
        import capo_pcs.types.update_cluster_slurm_configuration_request

        out["slurmConfiguration"] = (
            capo_pcs.types.update_cluster_slurm_configuration_request.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateClusterRequest:
    out: UpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("UpdateClusterRequest.cluster_identifier required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "slurmConfiguration" in data:
        import capo_pcs.types.update_cluster_slurm_configuration_request

        out["slurm_configuration"] = (
            capo_pcs.types.update_cluster_slurm_configuration_request.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    return out
