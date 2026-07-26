"""Generated from Smithy shape ``com.amazonaws.batch#TaskContainerDependency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class TaskContainerDependency(TypedDict, closed=True):
    container_name: NotRequired["capo_batch.types.string.String"]
    """<p>A unique identifier for the container.</p>"""
    condition: NotRequired["capo_batch.types.string.String"]
    """<p>The dependency condition of the container. The following are the available conditions and their behavior:</p> <ul> <li> <p> <code>START</code> - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start. </p> </li> <li> <p> <code>COMPLETE</code> - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. This condition can't be set on an essential container. </p> </li> <li> <p> <code>SUCCESS</code> - This condition is the same as <code>COMPLETE</code>, but it also requires that the container exits with a zero status. This condition can't be set on an essential container. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskContainerDependency) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "condition" in value:
        out["condition"] = value["condition"]
    return out


def deserialize_json(data: dict) -> TaskContainerDependency:
    out: TaskContainerDependency = {}  # type: ignore[typeddict-item]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    if "condition" in data:
        out["condition"] = data["condition"]
    return out
