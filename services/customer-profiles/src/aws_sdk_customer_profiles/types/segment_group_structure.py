"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentGroupStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.include_options
    import aws_sdk_customer_profiles.types.segment_group_list


class SegmentGroupStructure(TypedDict, closed=True):
    groups: NotRequired[
        "aws_sdk_customer_profiles.types.segment_group_list.SegmentGroupList"
    ]
    """<p>Holds the list of groups within the segment definition.</p>"""
    include: NotRequired[
        "aws_sdk_customer_profiles.types.include_options.IncludeOptions"
    ]
    """<p>Define whether to include or exclude the profiles that fit the segment criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentGroupStructure) -> dict:
    out: dict = {}
    if "groups" in value:
        import aws_sdk_customer_profiles.types.segment_group_list

        out["Groups"] = (
            aws_sdk_customer_profiles.types.segment_group_list.serialize_json(
                value["groups"]
            )
        )
    if "include" in value:
        import aws_sdk_customer_profiles.types.include_options

        out["Include"] = aws_sdk_customer_profiles.types.include_options.serialize_json(
            value["include"]
        )
    return out


def deserialize_json(data: dict) -> SegmentGroupStructure:
    out: SegmentGroupStructure = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import aws_sdk_customer_profiles.types.segment_group_list

        out["groups"] = (
            aws_sdk_customer_profiles.types.segment_group_list.deserialize_json(
                data["Groups"]
            )
        )
    if "Include" in data:
        import aws_sdk_customer_profiles.types.include_options

        out["include"] = (
            aws_sdk_customer_profiles.types.include_options.deserialize_json(
                data["Include"]
            )
        )
    return out
