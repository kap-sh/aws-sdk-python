"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Trails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.trail_info

Trails: TypeAlias = list["capo_cloudtrail.types.trail_info.TrailInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Trails) -> list:
    import capo_cloudtrail.types.trail_info

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.trail_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Trails:
    import capo_cloudtrail.types.trail_info

    out: Trails = []
    for item in data:
        out.append(capo_cloudtrail.types.trail_info.deserialize_aws_json_1_1(item))
    return out
