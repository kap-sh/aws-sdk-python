"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_arn
    import capo_networkmanager.types.core_network_edge_list
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.core_network_network_function_group_list
    import capo_networkmanager.types.core_network_segment_list
    import capo_networkmanager.types.core_network_state
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.tag_list


class CoreNetwork(TypedDict, closed=True):
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network that your core network is a part of. </p>"""
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    core_network_arn: NotRequired[
        "capo_networkmanager.types.core_network_arn.CoreNetworkArn"
    ]
    """<p>The ARN of a core network.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of a core network.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp when a core network was created.</p>"""
    state: NotRequired["capo_networkmanager.types.core_network_state.CoreNetworkState"]
    """<p>The current state of a core network.</p>"""
    segments: NotRequired[
        "capo_networkmanager.types.core_network_segment_list.CoreNetworkSegmentList"
    ]
    """<p>The segments within a core network.</p>"""
    network_function_groups: NotRequired[
        "capo_networkmanager.types.core_network_network_function_group_list.CoreNetworkNetworkFunctionGroupList"
    ]
    """<p>The network function groups associated with a core network.</p>"""
    edges: NotRequired[
        "capo_networkmanager.types.core_network_edge_list.CoreNetworkEdgeList"
    ]
    """<p>The edges within a core network.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with a core network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetwork) -> dict:
    out: dict = {}
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "core_network_arn" in value:
        out["CoreNetworkArn"] = value["core_network_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import capo_networkmanager.types.core_network_state

        out["State"] = capo_networkmanager.types.core_network_state.serialize_json(
            value["state"]
        )
    if "segments" in value:
        import capo_networkmanager.types.core_network_segment_list

        out["Segments"] = (
            capo_networkmanager.types.core_network_segment_list.serialize_json(
                value["segments"]
            )
        )
    if "network_function_groups" in value:
        import capo_networkmanager.types.core_network_network_function_group_list

        out["NetworkFunctionGroups"] = (
            capo_networkmanager.types.core_network_network_function_group_list.serialize_json(
                value["network_function_groups"]
            )
        )
    if "edges" in value:
        import capo_networkmanager.types.core_network_edge_list

        out["Edges"] = capo_networkmanager.types.core_network_edge_list.serialize_json(
            value["edges"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CoreNetwork:
    out: CoreNetwork = {}  # type: ignore[typeddict-item]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "CoreNetworkArn" in data:
        out["core_network_arn"] = data["CoreNetworkArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "State" in data:
        import capo_networkmanager.types.core_network_state

        out["state"] = capo_networkmanager.types.core_network_state.deserialize_json(
            data["State"]
        )
    if "Segments" in data:
        import capo_networkmanager.types.core_network_segment_list

        out["segments"] = (
            capo_networkmanager.types.core_network_segment_list.deserialize_json(
                data["Segments"]
            )
        )
    if "NetworkFunctionGroups" in data:
        import capo_networkmanager.types.core_network_network_function_group_list

        out["network_function_groups"] = (
            capo_networkmanager.types.core_network_network_function_group_list.deserialize_json(
                data["NetworkFunctionGroups"]
            )
        )
    if "Edges" in data:
        import capo_networkmanager.types.core_network_edge_list

        out["edges"] = (
            capo_networkmanager.types.core_network_edge_list.deserialize_json(
                data["Edges"]
            )
        )
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out
