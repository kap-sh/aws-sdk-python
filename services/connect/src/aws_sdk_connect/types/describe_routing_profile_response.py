"""Generated from Smithy shape ``com.amazonaws.connect#DescribeRoutingProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_profile


class DescribeRoutingProfileResponse(TypedDict):
    routing_profile: NotRequired["aws_sdk_connect.types.routing_profile.RoutingProfile"]
    """<p>The routing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRoutingProfileResponse) -> dict:
    out: dict = {}
    if "routing_profile" in value:
        import aws_sdk_connect.types.routing_profile

        out["RoutingProfile"] = aws_sdk_connect.types.routing_profile.serialize_json(
            value["routing_profile"]
        )
    return out


def deserialize_json(data: dict) -> DescribeRoutingProfileResponse:
    out: DescribeRoutingProfileResponse = {}  # type: ignore[typeddict-item]
    if "RoutingProfile" in data:
        import aws_sdk_connect.types.routing_profile

        out["routing_profile"] = aws_sdk_connect.types.routing_profile.deserialize_json(
            data["RoutingProfile"]
        )
    return out
