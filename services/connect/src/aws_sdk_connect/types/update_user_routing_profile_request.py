"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserRoutingProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.routing_profile_id
    import aws_sdk_connect.types.user_id


class UpdateUserRoutingProfileRequest(TypedDict):
    routing_profile_id: "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile for the user.</p>"""
    user_id: "aws_sdk_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRoutingProfileRequest) -> dict:
    out: dict = {}
    out["RoutingProfileId"] = value["routing_profile_id"]
    return out


def deserialize_json(data: dict) -> UpdateUserRoutingProfileRequest:
    out: UpdateUserRoutingProfileRequest = {}  # type: ignore[typeddict-item]
    if "RoutingProfileId" in data:
        out["routing_profile_id"] = data["RoutingProfileId"]
    else:
        raise DeserializationError(
            "UpdateUserRoutingProfileRequest.routing_profile_id required"
        )
    return out
