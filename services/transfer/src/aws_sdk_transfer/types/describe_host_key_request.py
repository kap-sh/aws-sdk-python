"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeHostKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.host_key_id
    import aws_sdk_transfer.types.server_id


class DescribeHostKeyRequest(TypedDict):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that contains the host key that you want described.</p>"""
    host_key_id: "aws_sdk_transfer.types.host_key_id.HostKeyId"
    """<p>The identifier of the host key that you want described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHostKeyRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["HostKeyId"] = value["host_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHostKeyRequest:
    out: DescribeHostKeyRequest = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("DescribeHostKeyRequest.server_id required")
    if "HostKeyId" in data:
        out["host_key_id"] = data["HostKeyId"]
    else:
        raise DeserializationError("DescribeHostKeyRequest.host_key_id required")
    return out
