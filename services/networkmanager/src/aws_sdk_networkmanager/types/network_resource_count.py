"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkResourceCount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.integer


class NetworkResourceCount(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The resource type.</p>"""
    count: NotRequired["aws_sdk_networkmanager.types.integer.Integer"]
    """<p>The resource count.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkResourceCount) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_json(data: dict) -> NetworkResourceCount:
    out: NetworkResourceCount = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "Count" in data:
        out["count"] = data["Count"]
    return out
