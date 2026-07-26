"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.include_options
    import capo_customer_profiles.types.segment_group_list


class SegmentGroup(TypedDict, closed=True):
    groups: NotRequired[
        "capo_customer_profiles.types.segment_group_list.SegmentGroupList"
    ]
    """<p>Holds the list of groups within the segment definition.</p>"""
    include: "capo_customer_profiles.types.include_options.IncludeOptions"
    """<p>Defines whether to include or exclude the profiles that fit the segment criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentGroup) -> dict:
    out: dict = {}
    if "groups" in value:
        import capo_customer_profiles.types.segment_group_list

        out["Groups"] = capo_customer_profiles.types.segment_group_list.serialize_json(
            value["groups"]
        )
    import capo_customer_profiles.types.include_options

    out["Include"] = capo_customer_profiles.types.include_options.serialize_json(
        value.get("include", "ALL")
    )
    return out


def deserialize_json(data: dict) -> SegmentGroup:
    out: SegmentGroup = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import capo_customer_profiles.types.segment_group_list

        out["groups"] = (
            capo_customer_profiles.types.segment_group_list.deserialize_json(
                data["Groups"]
            )
        )
    if "Include" in data:
        import capo_customer_profiles.types.include_options

        out["include"] = capo_customer_profiles.types.include_options.deserialize_json(
            data["Include"]
        )
    else:
        out["include"] = "ALL"
    return out
