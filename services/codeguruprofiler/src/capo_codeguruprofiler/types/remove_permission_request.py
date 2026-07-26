"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#RemovePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.action_group
    import capo_codeguruprofiler.types.profiling_group_name
    import capo_codeguruprofiler.types.revision_id


class RemovePermissionRequest(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group.</p>"""
    action_group: "capo_codeguruprofiler.types.action_group.ActionGroup"
    """<p> Specifies an action group that contains the permissions to remove from a profiling group's resource-based policy. One action group is supported, <code>agentPermissions</code>, which grants <code>ConfigureAgent</code> and <code>PostAgentProfile</code> permissions. </p>"""
    revision_id: "capo_codeguruprofiler.types.revision_id.RevisionId"
    """<p> A universally unique identifier (UUID) for the revision of the resource-based policy from which you want to remove permissions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemovePermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemovePermissionRequest:
    out: RemovePermissionRequest = {}  # type: ignore[typeddict-item]
    return out
