"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyPath``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group_summary


class HierarchyPath(TypedDict):
    level_one: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level one.</p>"""
    level_two: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level two.</p>"""
    level_three: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level three.</p>"""
    level_four: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level four.</p>"""
    level_five: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level five.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyPath) -> dict:
    out: dict = {}
    if "level_one" in value:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["LevelOne"] = aws_sdk_connect.types.hierarchy_group_summary.serialize_json(
            value["level_one"]
        )
    if "level_two" in value:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["LevelTwo"] = aws_sdk_connect.types.hierarchy_group_summary.serialize_json(
            value["level_two"]
        )
    if "level_three" in value:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["LevelThree"] = (
            aws_sdk_connect.types.hierarchy_group_summary.serialize_json(
                value["level_three"]
            )
        )
    if "level_four" in value:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["LevelFour"] = aws_sdk_connect.types.hierarchy_group_summary.serialize_json(
            value["level_four"]
        )
    if "level_five" in value:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["LevelFive"] = aws_sdk_connect.types.hierarchy_group_summary.serialize_json(
            value["level_five"]
        )
    return out


def deserialize_json(data: dict) -> HierarchyPath:
    out: HierarchyPath = {}  # type: ignore[typeddict-item]
    if "LevelOne" in data:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["level_one"] = (
            aws_sdk_connect.types.hierarchy_group_summary.deserialize_json(
                data["LevelOne"]
            )
        )
    if "LevelTwo" in data:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["level_two"] = (
            aws_sdk_connect.types.hierarchy_group_summary.deserialize_json(
                data["LevelTwo"]
            )
        )
    if "LevelThree" in data:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["level_three"] = (
            aws_sdk_connect.types.hierarchy_group_summary.deserialize_json(
                data["LevelThree"]
            )
        )
    if "LevelFour" in data:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["level_four"] = (
            aws_sdk_connect.types.hierarchy_group_summary.deserialize_json(
                data["LevelFour"]
            )
        )
    if "LevelFive" in data:
        import aws_sdk_connect.types.hierarchy_group_summary

        out["level_five"] = (
            aws_sdk_connect.types.hierarchy_group_summary.deserialize_json(
                data["LevelFive"]
            )
        )
    return out
