"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRoutingProfileNameRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.routing_profile_description
    import aws_sdk_connect.types.routing_profile_id
    import aws_sdk_connect.types.routing_profile_name


class UpdateRoutingProfileNameRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    name: NotRequired["aws_sdk_connect.types.routing_profile_name.RoutingProfileName"]
    """<p>The name of the routing profile. Must not be more than 127 characters.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.routing_profile_description.RoutingProfileDescription"
    ]
    """<p>The description of the routing profile. Must not be more than 250 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingProfileNameRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateRoutingProfileNameRequest:
    out: UpdateRoutingProfileNameRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
