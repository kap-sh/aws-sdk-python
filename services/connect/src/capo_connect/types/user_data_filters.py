"""Generated from Smithy shape ``com.amazonaws.connect#UserDataFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agents_min_one_max_hundred
    import capo_connect.types.contact_filter
    import capo_connect.types.queues
    import capo_connect.types.routing_profiles
    import capo_connect.types.user_data_hierarchy_groups


class UserDataFilters(TypedDict, closed=True):
    queues: NotRequired["capo_connect.types.queues.Queues"]
    """<p>A list of up to 100 queues or ARNs.</p>"""
    contact_filter: NotRequired["capo_connect.types.contact_filter.ContactFilter"]
    """<p>A filter for the user data based on the contact information that is associated to the user. It contains a list of contact states. </p>"""
    routing_profiles: NotRequired["capo_connect.types.routing_profiles.RoutingProfiles"]
    """<p>A list of up to 100 routing profile IDs or ARNs.</p>"""
    agents: NotRequired[
        "capo_connect.types.agents_min_one_max_hundred.AgentsMinOneMaxHundred"
    ]
    """<p>A list of up to 100 agent IDs or ARNs.</p>"""
    user_hierarchy_groups: NotRequired[
        "capo_connect.types.user_data_hierarchy_groups.UserDataHierarchyGroups"
    ]
    """<p>A UserHierarchyGroup ID or ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserDataFilters) -> dict:
    out: dict = {}
    if "queues" in value:
        import capo_connect.types.queues

        out["Queues"] = capo_connect.types.queues.serialize_json(value["queues"])
    if "contact_filter" in value:
        import capo_connect.types.contact_filter

        out["ContactFilter"] = capo_connect.types.contact_filter.serialize_json(
            value["contact_filter"]
        )
    if "routing_profiles" in value:
        import capo_connect.types.routing_profiles

        out["RoutingProfiles"] = capo_connect.types.routing_profiles.serialize_json(
            value["routing_profiles"]
        )
    if "agents" in value:
        import capo_connect.types.agents_min_one_max_hundred

        out["Agents"] = capo_connect.types.agents_min_one_max_hundred.serialize_json(
            value["agents"]
        )
    if "user_hierarchy_groups" in value:
        import capo_connect.types.user_data_hierarchy_groups

        out["UserHierarchyGroups"] = (
            capo_connect.types.user_data_hierarchy_groups.serialize_json(
                value["user_hierarchy_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserDataFilters:
    out: UserDataFilters = {}  # type: ignore[typeddict-item]
    if "Queues" in data:
        import capo_connect.types.queues

        out["queues"] = capo_connect.types.queues.deserialize_json(data["Queues"])
    if "ContactFilter" in data:
        import capo_connect.types.contact_filter

        out["contact_filter"] = capo_connect.types.contact_filter.deserialize_json(
            data["ContactFilter"]
        )
    if "RoutingProfiles" in data:
        import capo_connect.types.routing_profiles

        out["routing_profiles"] = capo_connect.types.routing_profiles.deserialize_json(
            data["RoutingProfiles"]
        )
    if "Agents" in data:
        import capo_connect.types.agents_min_one_max_hundred

        out["agents"] = capo_connect.types.agents_min_one_max_hundred.deserialize_json(
            data["Agents"]
        )
    if "UserHierarchyGroups" in data:
        import capo_connect.types.user_data_hierarchy_groups

        out["user_hierarchy_groups"] = (
            capo_connect.types.user_data_hierarchy_groups.deserialize_json(
                data["UserHierarchyGroups"]
            )
        )
    return out
