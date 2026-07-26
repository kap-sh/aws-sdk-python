"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group_summary


class HierarchyPath(TypedDict, closed=True):
    level_one: NotRequired[
        "capo_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level one.</p>"""
    level_two: NotRequired[
        "capo_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level two.</p>"""
    level_three: NotRequired[
        "capo_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level three.</p>"""
    level_four: NotRequired[
        "capo_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level four.</p>"""
    level_five: NotRequired[
        "capo_connect.types.hierarchy_group_summary.HierarchyGroupSummary"
    ]
    """<p>Information about level five.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyPath) -> dict:
    out: dict = {}
    if "level_one" in value:
        import capo_connect.types.hierarchy_group_summary

        out["LevelOne"] = capo_connect.types.hierarchy_group_summary.serialize_json(
            value["level_one"]
        )
    if "level_two" in value:
        import capo_connect.types.hierarchy_group_summary

        out["LevelTwo"] = capo_connect.types.hierarchy_group_summary.serialize_json(
            value["level_two"]
        )
    if "level_three" in value:
        import capo_connect.types.hierarchy_group_summary

        out["LevelThree"] = capo_connect.types.hierarchy_group_summary.serialize_json(
            value["level_three"]
        )
    if "level_four" in value:
        import capo_connect.types.hierarchy_group_summary

        out["LevelFour"] = capo_connect.types.hierarchy_group_summary.serialize_json(
            value["level_four"]
        )
    if "level_five" in value:
        import capo_connect.types.hierarchy_group_summary

        out["LevelFive"] = capo_connect.types.hierarchy_group_summary.serialize_json(
            value["level_five"]
        )
    return out


def deserialize_json(data: dict) -> HierarchyPath:
    out: HierarchyPath = {}  # type: ignore[typeddict-item]
    if "LevelOne" in data:
        import capo_connect.types.hierarchy_group_summary

        out["level_one"] = capo_connect.types.hierarchy_group_summary.deserialize_json(
            data["LevelOne"]
        )
    if "LevelTwo" in data:
        import capo_connect.types.hierarchy_group_summary

        out["level_two"] = capo_connect.types.hierarchy_group_summary.deserialize_json(
            data["LevelTwo"]
        )
    if "LevelThree" in data:
        import capo_connect.types.hierarchy_group_summary

        out["level_three"] = (
            capo_connect.types.hierarchy_group_summary.deserialize_json(
                data["LevelThree"]
            )
        )
    if "LevelFour" in data:
        import capo_connect.types.hierarchy_group_summary

        out["level_four"] = capo_connect.types.hierarchy_group_summary.deserialize_json(
            data["LevelFour"]
        )
    if "LevelFive" in data:
        import capo_connect.types.hierarchy_group_summary

        out["level_five"] = capo_connect.types.hierarchy_group_summary.deserialize_json(
            data["LevelFive"]
        )
    return out
