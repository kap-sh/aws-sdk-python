"""Generated from Smithy shape ``com.amazonaws.connect#DescribeRoutingProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.routing_profile


class DescribeRoutingProfileResponse(TypedDict, closed=True):
    routing_profile: NotRequired["capo_connect.types.routing_profile.RoutingProfile"]
    """<p>The routing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRoutingProfileResponse) -> dict:
    out: dict = {}
    if "routing_profile" in value:
        import capo_connect.types.routing_profile

        out["RoutingProfile"] = capo_connect.types.routing_profile.serialize_json(
            value["routing_profile"]
        )
    return out


def deserialize_json(data: dict) -> DescribeRoutingProfileResponse:
    out: DescribeRoutingProfileResponse = {}  # type: ignore[typeddict-item]
    if "RoutingProfile" in data:
        import capo_connect.types.routing_profile

        out["routing_profile"] = capo_connect.types.routing_profile.deserialize_json(
            data["RoutingProfile"]
        )
    return out
