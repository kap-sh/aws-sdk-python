"""Generated from Smithy shape ``com.amazonaws.cloudtrail#TrailInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.string


class TrailInfo(TypedDict):
    trail_arn: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The ARN of a trail.</p>"""
    name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The name of a trail.</p>"""
    home_region: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The Amazon Web Services Region in which a trail was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrailInfo) -> dict:
    out: dict = {}
    if "trail_arn" in value:
        out["TrailARN"] = value["trail_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrailInfo:
    out: TrailInfo = {}  # type: ignore[typeddict-item]
    if "TrailARN" in data:
        out["trail_arn"] = data["TrailARN"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    return out
