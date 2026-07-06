"""Generated from Smithy shape ``com.amazonaws.snowball#CompatibleImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.string


class CompatibleImage(TypedDict, closed=True):
    ami_id: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The unique identifier for an individual Snow device AMI.</p>"""
    name: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The optional name of a compatible image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompatibleImage) -> dict:
    out: dict = {}
    if "ami_id" in value:
        out["AmiId"] = value["ami_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CompatibleImage:
    out: CompatibleImage = {}  # type: ignore[typeddict-item]
    if "AmiId" in data:
        out["ami_id"] = data["AmiId"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
