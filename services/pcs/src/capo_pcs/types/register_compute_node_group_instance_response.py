"""Generated from Smithy shape ``com.amazonaws.pcs#RegisterComputeNodeGroupInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.endpoints
    import capo_pcs.types.shared_secret


class RegisterComputeNodeGroupInstanceResponse(TypedDict, closed=True):
    node_id: "str"
    """<p>The scheduler node ID for this instance.</p>"""
    shared_secret: "capo_pcs.types.shared_secret.SharedSecret"
    """<p>For the Slurm scheduler, this is the shared Munge key the scheduler uses to authenticate compute node group instances.</p>"""
    endpoints: "capo_pcs.types.endpoints.Endpoints"
    """<p>The list of endpoints available for interaction with the scheduler.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegisterComputeNodeGroupInstanceResponse) -> dict:
    out: dict = {}
    out["nodeID"] = value["node_id"]
    out["sharedSecret"] = value["shared_secret"]
    import capo_pcs.types.endpoints

    out["endpoints"] = capo_pcs.types.endpoints.serialize_aws_json_1_0(
        value["endpoints"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegisterComputeNodeGroupInstanceResponse:
    out: RegisterComputeNodeGroupInstanceResponse = {}  # type: ignore[typeddict-item]
    if "nodeID" in data:
        out["node_id"] = data["nodeID"]
    else:
        raise DeserializationError(
            "RegisterComputeNodeGroupInstanceResponse.node_id required"
        )
    if "sharedSecret" in data:
        out["shared_secret"] = data["sharedSecret"]
    else:
        raise DeserializationError(
            "RegisterComputeNodeGroupInstanceResponse.shared_secret required"
        )
    if "endpoints" in data:
        import capo_pcs.types.endpoints

        out["endpoints"] = capo_pcs.types.endpoints.deserialize_aws_json_1_0(
            data["endpoints"]
        )
    else:
        raise DeserializationError(
            "RegisterComputeNodeGroupInstanceResponse.endpoints required"
        )
    return out
