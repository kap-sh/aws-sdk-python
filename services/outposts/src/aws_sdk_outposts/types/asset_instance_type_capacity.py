"""Generated from Smithy shape ``com.amazonaws.outposts#AssetInstanceTypeCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.instance_type_count
    import aws_sdk_outposts.types.instance_type_name


class AssetInstanceTypeCapacity(TypedDict, closed=True):
    instance_type: "aws_sdk_outposts.types.instance_type_name.InstanceTypeName"
    """<p>The type of instance.</p>"""
    count: "aws_sdk_outposts.types.instance_type_count.InstanceTypeCount"
    """<p>The number of each instance type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetInstanceTypeCapacity) -> dict:
    out: dict = {}
    out["InstanceType"] = value["instance_type"]
    out["Count"] = value.get("count", 0)
    return out


def deserialize_json(data: dict) -> AssetInstanceTypeCapacity:
    out: AssetInstanceTypeCapacity = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    else:
        raise DeserializationError("AssetInstanceTypeCapacity.instance_type required")
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    return out
