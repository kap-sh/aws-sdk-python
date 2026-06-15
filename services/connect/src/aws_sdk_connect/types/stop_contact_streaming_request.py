"""Generated from Smithy shape ``com.amazonaws.connect#StopContactStreamingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.streaming_id


class StopContactStreamingRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact. This is the identifier of the contact that is associated with the first interaction with the contact center.</p>"""
    streaming_id: "aws_sdk_connect.types.streaming_id.StreamingId"
    """<p>The identifier of the streaming configuration enabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopContactStreamingRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    out["StreamingId"] = value["streaming_id"]
    return out


def deserialize_json(data: dict) -> StopContactStreamingRequest:
    out: StopContactStreamingRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StopContactStreamingRequest.instance_id required")
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("StopContactStreamingRequest.contact_id required")
    if "StreamingId" in data:
        out["streaming_id"] = data["StreamingId"]
    else:
        raise DeserializationError("StopContactStreamingRequest.streaming_id required")
    return out
