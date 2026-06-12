"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.cluster_network_settings_update_request


class UpdateClusterRequest(TypedDict):
    cluster_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the cluster"""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Include this parameter only if you want to change the current name of the Cluster. Specify a name that is unique in the AWS account. You can't change the name. Names are case-sensitive."""
    network_settings: NotRequired[
        "aws_sdk_medialive.types.cluster_network_settings_update_request.ClusterNetworkSettingsUpdateRequest"
    ]
    """Include this property only if you want to change the current connections between the Nodes in the Cluster and the Networks the Cluster is associated with."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "network_settings" in value:
        import aws_sdk_medialive.types.cluster_network_settings_update_request

        out["networkSettings"] = (
            aws_sdk_medialive.types.cluster_network_settings_update_request.serialize_json(
                value["network_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateClusterRequest:
    out: UpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "networkSettings" in data:
        import aws_sdk_medialive.types.cluster_network_settings_update_request

        out["network_settings"] = (
            aws_sdk_medialive.types.cluster_network_settings_update_request.deserialize_json(
                data["networkSettings"]
            )
        )
    return out
