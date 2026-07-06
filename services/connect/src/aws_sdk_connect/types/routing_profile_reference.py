"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.routing_profile_id


class RoutingProfileReference(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.routing_profile_id.RoutingProfileId"]
    """<p>The identifier of the routing profile.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the routing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileReference) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> RoutingProfileReference:
    out: RoutingProfileReference = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
