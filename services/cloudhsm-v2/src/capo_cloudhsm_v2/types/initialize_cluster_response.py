"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#InitializeClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cluster_state
    import capo_cloudhsm_v2.types.state_message


class InitializeClusterResponse(TypedDict, closed=True):
    state: NotRequired["capo_cloudhsm_v2.types.cluster_state.ClusterState"]
    """<p>The cluster's state.</p>"""
    state_message: NotRequired["capo_cloudhsm_v2.types.state_message.StateMessage"]
    """<p>A description of the cluster's state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InitializeClusterResponse) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_cloudhsm_v2.types.cluster_state

        out["State"] = capo_cloudhsm_v2.types.cluster_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_message" in value:
        out["StateMessage"] = value["state_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InitializeClusterResponse:
    out: InitializeClusterResponse = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import capo_cloudhsm_v2.types.cluster_state

        out["state"] = capo_cloudhsm_v2.types.cluster_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateMessage" in data:
        out["state_message"] = data["StateMessage"]
    return out
