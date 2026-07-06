"""Generated from Smithy shape ``com.amazonaws.groundstation#MissionProfileListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.aws_region
    import aws_sdk_groundstation.types.mission_profile_arn
    import aws_sdk_groundstation.types.safe_name
    import aws_sdk_groundstation.types.uuid


class MissionProfileListItem(TypedDict, closed=True):
    mission_profile_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of a mission profile.</p>"""
    mission_profile_arn: NotRequired[
        "aws_sdk_groundstation.types.mission_profile_arn.MissionProfileArn"
    ]
    """<p>ARN of a mission profile.</p>"""
    region: NotRequired["aws_sdk_groundstation.types.aws_region.AWSRegion"]
    """<p>Region of a mission profile.</p>"""
    name: NotRequired["aws_sdk_groundstation.types.safe_name.SafeName"]
    """<p>Name of a mission profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissionProfileListItem) -> dict:
    out: dict = {}
    if "mission_profile_id" in value:
        out["missionProfileId"] = value["mission_profile_id"]
    if "mission_profile_arn" in value:
        out["missionProfileArn"] = value["mission_profile_arn"]
    if "region" in value:
        out["region"] = value["region"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> MissionProfileListItem:
    out: MissionProfileListItem = {}  # type: ignore[typeddict-item]
    if "missionProfileId" in data:
        out["mission_profile_id"] = data["missionProfileId"]
    if "missionProfileArn" in data:
        out["mission_profile_arn"] = data["missionProfileArn"]
    if "region" in data:
        out["region"] = data["region"]
    if "name" in data:
        out["name"] = data["name"]
    return out
