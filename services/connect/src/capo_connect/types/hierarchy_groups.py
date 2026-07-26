"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_hierarchy_group


class HierarchyGroups(TypedDict, closed=True):
    level1: NotRequired["capo_connect.types.agent_hierarchy_group.AgentHierarchyGroup"]
    """<p>The group at level one of the agent hierarchy.</p>"""
    level2: NotRequired["capo_connect.types.agent_hierarchy_group.AgentHierarchyGroup"]
    """<p>The group at level two of the agent hierarchy.</p>"""
    level3: NotRequired["capo_connect.types.agent_hierarchy_group.AgentHierarchyGroup"]
    """<p>The group at level three of the agent hierarchy.</p>"""
    level4: NotRequired["capo_connect.types.agent_hierarchy_group.AgentHierarchyGroup"]
    """<p>The group at level four of the agent hierarchy.</p>"""
    level5: NotRequired["capo_connect.types.agent_hierarchy_group.AgentHierarchyGroup"]
    """<p>The group at level five of the agent hierarchy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyGroups) -> dict:
    out: dict = {}
    if "level1" in value:
        import capo_connect.types.agent_hierarchy_group

        out["Level1"] = capo_connect.types.agent_hierarchy_group.serialize_json(
            value["level1"]
        )
    if "level2" in value:
        import capo_connect.types.agent_hierarchy_group

        out["Level2"] = capo_connect.types.agent_hierarchy_group.serialize_json(
            value["level2"]
        )
    if "level3" in value:
        import capo_connect.types.agent_hierarchy_group

        out["Level3"] = capo_connect.types.agent_hierarchy_group.serialize_json(
            value["level3"]
        )
    if "level4" in value:
        import capo_connect.types.agent_hierarchy_group

        out["Level4"] = capo_connect.types.agent_hierarchy_group.serialize_json(
            value["level4"]
        )
    if "level5" in value:
        import capo_connect.types.agent_hierarchy_group

        out["Level5"] = capo_connect.types.agent_hierarchy_group.serialize_json(
            value["level5"]
        )
    return out


def deserialize_json(data: dict) -> HierarchyGroups:
    out: HierarchyGroups = {}  # type: ignore[typeddict-item]
    if "Level1" in data:
        import capo_connect.types.agent_hierarchy_group

        out["level1"] = capo_connect.types.agent_hierarchy_group.deserialize_json(
            data["Level1"]
        )
    if "Level2" in data:
        import capo_connect.types.agent_hierarchy_group

        out["level2"] = capo_connect.types.agent_hierarchy_group.deserialize_json(
            data["Level2"]
        )
    if "Level3" in data:
        import capo_connect.types.agent_hierarchy_group

        out["level3"] = capo_connect.types.agent_hierarchy_group.deserialize_json(
            data["Level3"]
        )
    if "Level4" in data:
        import capo_connect.types.agent_hierarchy_group

        out["level4"] = capo_connect.types.agent_hierarchy_group.deserialize_json(
            data["Level4"]
        )
    if "Level5" in data:
        import capo_connect.types.agent_hierarchy_group

        out["level5"] = capo_connect.types.agent_hierarchy_group.deserialize_json(
            data["Level5"]
        )
    return out
