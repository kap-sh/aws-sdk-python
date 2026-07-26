"""Generated from Smithy shape ``com.amazonaws.networkmanager#Via``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.network_function_group_list
    import capo_networkmanager.types.with_edge_overrides_list


class Via(TypedDict, closed=True):
    network_function_groups: NotRequired[
        "capo_networkmanager.types.network_function_group_list.NetworkFunctionGroupList"
    ]
    """<p>The list of network function groups associated with the service insertion action.</p>"""
    with_edge_overrides: NotRequired[
        "capo_networkmanager.types.with_edge_overrides_list.WithEdgeOverridesList"
    ]
    """<p>Describes any edge overrides. An edge override is a specific edge to be used for traffic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Via) -> dict:
    out: dict = {}
    if "network_function_groups" in value:
        import capo_networkmanager.types.network_function_group_list

        out["NetworkFunctionGroups"] = (
            capo_networkmanager.types.network_function_group_list.serialize_json(
                value["network_function_groups"]
            )
        )
    if "with_edge_overrides" in value:
        import capo_networkmanager.types.with_edge_overrides_list

        out["WithEdgeOverrides"] = (
            capo_networkmanager.types.with_edge_overrides_list.serialize_json(
                value["with_edge_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> Via:
    out: Via = {}  # type: ignore[typeddict-item]
    if "NetworkFunctionGroups" in data:
        import capo_networkmanager.types.network_function_group_list

        out["network_function_groups"] = (
            capo_networkmanager.types.network_function_group_list.deserialize_json(
                data["NetworkFunctionGroups"]
            )
        )
    if "WithEdgeOverrides" in data:
        import capo_networkmanager.types.with_edge_overrides_list

        out["with_edge_overrides"] = (
            capo_networkmanager.types.with_edge_overrides_list.deserialize_json(
                data["WithEdgeOverrides"]
            )
        )
    return out
