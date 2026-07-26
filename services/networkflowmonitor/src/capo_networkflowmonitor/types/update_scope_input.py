"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#UpdateScopeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.scope_id
    import capo_networkflowmonitor.types.target_resource_list


class UpdateScopeInput(TypedDict, closed=True):
    scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId"
    """<p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>"""
    resources_to_add: NotRequired[
        "capo_networkflowmonitor.types.target_resource_list.TargetResourceList"
    ]
    """<p>A list of resources to add to a scope.</p>"""
    resources_to_delete: NotRequired[
        "capo_networkflowmonitor.types.target_resource_list.TargetResourceList"
    ]
    """<p>A list of resources to delete from a scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScopeInput) -> dict:
    out: dict = {}
    if "resources_to_add" in value:
        import capo_networkflowmonitor.types.target_resource_list

        out["resourcesToAdd"] = (
            capo_networkflowmonitor.types.target_resource_list.serialize_json(
                value["resources_to_add"]
            )
        )
    if "resources_to_delete" in value:
        import capo_networkflowmonitor.types.target_resource_list

        out["resourcesToDelete"] = (
            capo_networkflowmonitor.types.target_resource_list.serialize_json(
                value["resources_to_delete"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateScopeInput:
    out: UpdateScopeInput = {}  # type: ignore[typeddict-item]
    if "resourcesToAdd" in data:
        import capo_networkflowmonitor.types.target_resource_list

        out["resources_to_add"] = (
            capo_networkflowmonitor.types.target_resource_list.deserialize_json(
                data["resourcesToAdd"]
            )
        )
    if "resourcesToDelete" in data:
        import capo_networkflowmonitor.types.target_resource_list

        out["resources_to_delete"] = (
            capo_networkflowmonitor.types.target_resource_list.deserialize_json(
                data["resourcesToDelete"]
            )
        )
    return out
