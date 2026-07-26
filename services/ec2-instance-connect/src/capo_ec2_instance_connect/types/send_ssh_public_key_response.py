"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SendSSHPublicKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.request_id
    import capo_ec2_instance_connect.types.success


class SendSSHPublicKeyResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_ec2_instance_connect.types.request_id.RequestId"]
    """<p>The ID of the request. Please provide this ID when contacting AWS Support for assistance.</p>"""
    success: "capo_ec2_instance_connect.types.success.Success"
    """<p>Is true if the request succeeds and an error otherwise.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendSSHPublicKeyResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    out["Success"] = value.get("success", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> SendSSHPublicKeyResponse:
    out: SendSSHPublicKeyResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Success" in data:
        out["success"] = data["Success"]
    else:
        out["success"] = False
    return out
