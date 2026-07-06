"""Generated from Smithy shape ``com.amazonaws.inspector2#Ec2Metadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ami_id
    import aws_sdk_inspector2.types.ec2_platform
    import aws_sdk_inspector2.types.tag_map


class Ec2Metadata(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>The tags attached to the instance.</p>"""
    ami_id: NotRequired["aws_sdk_inspector2.types.ami_id.AmiId"]
    """<p>The ID of the Amazon Machine Image (AMI) used to launch the instance.</p>"""
    platform: NotRequired["aws_sdk_inspector2.types.ec2_platform.Ec2Platform"]
    """<p>The platform of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2Metadata) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.serialize_json(value["tags"])
    if "ami_id" in value:
        out["amiId"] = value["ami_id"]
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> Ec2Metadata:
    out: Ec2Metadata = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.deserialize_json(data["tags"])
    if "amiId" in data:
        out["ami_id"] = data["amiId"]
    if "platform" in data:
        out["platform"] = data["platform"]
    return out
