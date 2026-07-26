"""Generated from Smithy shape ``com.amazonaws.cloudtrail#TrailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.trail

TrailList: TypeAlias = list["capo_cloudtrail.types.trail.Trail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrailList) -> list:
    import capo_cloudtrail.types.trail

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.trail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TrailList:
    import capo_cloudtrail.types.trail

    out: TrailList = []
    for item in data:
        out.append(capo_cloudtrail.types.trail.deserialize_aws_json_1_1(item))
    return out
