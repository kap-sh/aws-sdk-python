"""Generated from Smithy shape ``com.amazonaws.connect#CreateRoutingProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.routing_profile_id


class CreateRoutingProfileResponse(TypedDict):
    routing_profile_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the routing profile.</p>"""
    routing_profile_id: NotRequired[
        "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    ]
    """<p>The identifier of the routing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoutingProfileResponse) -> dict:
    out: dict = {}
    if "routing_profile_arn" in value:
        out["RoutingProfileArn"] = value["routing_profile_arn"]
    if "routing_profile_id" in value:
        out["RoutingProfileId"] = value["routing_profile_id"]
    return out


def deserialize_json(data: dict) -> CreateRoutingProfileResponse:
    out: CreateRoutingProfileResponse = {}  # type: ignore[typeddict-item]
    if "RoutingProfileArn" in data:
        out["routing_profile_arn"] = data["RoutingProfileArn"]
    if "RoutingProfileId" in data:
        out["routing_profile_id"] = data["RoutingProfileId"]
    return out
