"""Generated from Smithy shape ``com.amazonaws.evs#AssociateEipToVlanRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_evs.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_evs.types.allocation_id
    import aws_sdk_evs.types.client_token
    import aws_sdk_evs.types.environment_id

class AssociateEipToVlanRequest(TypedDict):
    client_token: NotRequired["aws_sdk_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment containing the VLAN that the Elastic IP address associates with.</p>"""
    vlan_name: "str"
    """<p>The name of the VLAN. <code>hcx</code> is the only accepted VLAN name at this time.</p>"""
    allocation_id: "aws_sdk_evs.types.allocation_id.AllocationId"
    """<p>The Elastic IP address allocation ID.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateEipToVlanRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["environmentId"] = value["environment_id"]
    out["vlanName"] = value["vlan_name"]
    out["allocationId"] = value["allocation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateEipToVlanRequest:
    out: AssociateEipToVlanRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("AssociateEipToVlanRequest.environment_id required")
    if "vlanName" in data:
        out["vlan_name"] = data["vlanName"]
    else:
        raise DeserializationError("AssociateEipToVlanRequest.vlan_name required")
    if "allocationId" in data:
        out["allocation_id"] = data["allocationId"]
    else:
        raise DeserializationError("AssociateEipToVlanRequest.allocation_id required")
    return out