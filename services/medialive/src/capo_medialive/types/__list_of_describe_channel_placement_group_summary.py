"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDescribeChannelPlacementGroupSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.describe_channel_placement_group_summary

__listOfDescribeChannelPlacementGroupSummary: TypeAlias = list[
    "capo_medialive.types.describe_channel_placement_group_summary.DescribeChannelPlacementGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDescribeChannelPlacementGroupSummary) -> list:
    import capo_medialive.types.describe_channel_placement_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.describe_channel_placement_group_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfDescribeChannelPlacementGroupSummary:
    import capo_medialive.types.describe_channel_placement_group_summary

    out: __listOfDescribeChannelPlacementGroupSummary = []
    for item in data:
        out.append(
            capo_medialive.types.describe_channel_placement_group_summary.deserialize_json(
                item
            )
        )
    return out
