"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListVirtualClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.boolean
    import aws_sdk_emr_containers.types.container_provider_type
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.java_integer
    import aws_sdk_emr_containers.types.next_token
    import aws_sdk_emr_containers.types.string1024
    import aws_sdk_emr_containers.types.virtual_cluster_states


class ListVirtualClustersRequest(TypedDict, closed=True):
    container_provider_id: NotRequired[
        "aws_sdk_emr_containers.types.string1024.String1024"
    ]
    """<p>The container provider ID of the virtual cluster.</p>"""
    container_provider_type: NotRequired[
        "aws_sdk_emr_containers.types.container_provider_type.ContainerProviderType"
    ]
    """<p>The container provider type of the virtual cluster. Amazon EKS is the only supported type as of now.</p>"""
    created_after: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time after which the virtual clusters are created.</p>"""
    created_before: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time before which the virtual clusters are created.</p>"""
    states: NotRequired[
        "aws_sdk_emr_containers.types.virtual_cluster_states.VirtualClusterStates"
    ]
    """<p>The states of the requested virtual clusters.</p>"""
    max_results: NotRequired["aws_sdk_emr_containers.types.java_integer.JavaInteger"]
    """<p>The maximum number of virtual clusters that can be listed.</p>"""
    next_token: NotRequired["aws_sdk_emr_containers.types.next_token.NextToken"]
    """<p>The token for the next set of virtual clusters to return. </p>"""
    eks_access_entry_integrated: NotRequired[
        "aws_sdk_emr_containers.types.boolean.Boolean"
    ]
    """<p>Optional Boolean that specifies whether the operation should return the virtual clusters that have the access entry integration enabled or disabled. If not specified, the operation returns all applicable virtual clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVirtualClustersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVirtualClustersRequest:
    out: ListVirtualClustersRequest = {}  # type: ignore[typeddict-item]
    return out
