"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyStructureUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_level_update


class HierarchyStructureUpdate(TypedDict, closed=True):
    level_one: NotRequired[
        "capo_connect.types.hierarchy_level_update.HierarchyLevelUpdate"
    ]
    """<p>The update for level one.</p>"""
    level_two: NotRequired[
        "capo_connect.types.hierarchy_level_update.HierarchyLevelUpdate"
    ]
    """<p>The update for level two.</p>"""
    level_three: NotRequired[
        "capo_connect.types.hierarchy_level_update.HierarchyLevelUpdate"
    ]
    """<p>The update for level three.</p>"""
    level_four: NotRequired[
        "capo_connect.types.hierarchy_level_update.HierarchyLevelUpdate"
    ]
    """<p>The update for level four.</p>"""
    level_five: NotRequired[
        "capo_connect.types.hierarchy_level_update.HierarchyLevelUpdate"
    ]
    """<p>The update for level five.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyStructureUpdate) -> dict:
    out: dict = {}
    if "level_one" in value:
        import capo_connect.types.hierarchy_level_update

        out["LevelOne"] = capo_connect.types.hierarchy_level_update.serialize_json(
            value["level_one"]
        )
    if "level_two" in value:
        import capo_connect.types.hierarchy_level_update

        out["LevelTwo"] = capo_connect.types.hierarchy_level_update.serialize_json(
            value["level_two"]
        )
    if "level_three" in value:
        import capo_connect.types.hierarchy_level_update

        out["LevelThree"] = capo_connect.types.hierarchy_level_update.serialize_json(
            value["level_three"]
        )
    if "level_four" in value:
        import capo_connect.types.hierarchy_level_update

        out["LevelFour"] = capo_connect.types.hierarchy_level_update.serialize_json(
            value["level_four"]
        )
    if "level_five" in value:
        import capo_connect.types.hierarchy_level_update

        out["LevelFive"] = capo_connect.types.hierarchy_level_update.serialize_json(
            value["level_five"]
        )
    return out


def deserialize_json(data: dict) -> HierarchyStructureUpdate:
    out: HierarchyStructureUpdate = {}  # type: ignore[typeddict-item]
    if "LevelOne" in data:
        import capo_connect.types.hierarchy_level_update

        out["level_one"] = capo_connect.types.hierarchy_level_update.deserialize_json(
            data["LevelOne"]
        )
    if "LevelTwo" in data:
        import capo_connect.types.hierarchy_level_update

        out["level_two"] = capo_connect.types.hierarchy_level_update.deserialize_json(
            data["LevelTwo"]
        )
    if "LevelThree" in data:
        import capo_connect.types.hierarchy_level_update

        out["level_three"] = capo_connect.types.hierarchy_level_update.deserialize_json(
            data["LevelThree"]
        )
    if "LevelFour" in data:
        import capo_connect.types.hierarchy_level_update

        out["level_four"] = capo_connect.types.hierarchy_level_update.deserialize_json(
            data["LevelFour"]
        )
    if "LevelFive" in data:
        import capo_connect.types.hierarchy_level_update

        out["level_five"] = capo_connect.types.hierarchy_level_update.deserialize_json(
            data["LevelFive"]
        )
    return out
