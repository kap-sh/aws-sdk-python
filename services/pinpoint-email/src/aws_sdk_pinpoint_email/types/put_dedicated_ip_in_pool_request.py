"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutDedicatedIpInPoolRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.ip
    import aws_sdk_pinpoint_email.types.pool_name


class PutDedicatedIpInPoolRequest(TypedDict):
    ip: "aws_sdk_pinpoint_email.types.ip.Ip"
    """<p>The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that's associated with your Amazon Pinpoint account.</p>"""
    destination_pool_name: "aws_sdk_pinpoint_email.types.pool_name.PoolName"
    """<p>The name of the IP pool that you want to add the dedicated IP address to. You have to specify an IP pool that already exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDedicatedIpInPoolRequest) -> dict:
    out: dict = {}
    out["DestinationPoolName"] = value["destination_pool_name"]
    return out


def deserialize_json(data: dict) -> PutDedicatedIpInPoolRequest:
    out: PutDedicatedIpInPoolRequest = {}  # type: ignore[typeddict-item]
    if "DestinationPoolName" in data:
        out["destination_pool_name"] = data["DestinationPoolName"]
    else:
        raise DeserializationError(
            "PutDedicatedIpInPoolRequest.destination_pool_name required"
        )
    return out
