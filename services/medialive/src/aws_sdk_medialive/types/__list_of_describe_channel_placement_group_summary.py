"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDescribeChannelPlacementGroupSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.describe_channel_placement_group_summary

__listOfDescribeChannelPlacementGroupSummary: TypeAlias = list[
    "aws_sdk_medialive.types.describe_channel_placement_group_summary.DescribeChannelPlacementGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDescribeChannelPlacementGroupSummary) -> list:
    import aws_sdk_medialive.types.describe_channel_placement_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.describe_channel_placement_group_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfDescribeChannelPlacementGroupSummary:
    import aws_sdk_medialive.types.describe_channel_placement_group_summary

    out: __listOfDescribeChannelPlacementGroupSummary = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.describe_channel_placement_group_summary.deserialize_json(
                item
            )
        )
    return out
