"""Generated from Smithy shape ``com.amazonaws.batch#TaskPropertiesOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.list_task_container_overrides


class TaskPropertiesOverride(TypedDict, closed=True):
    containers: NotRequired[
        "capo_batch.types.list_task_container_overrides.ListTaskContainerOverrides"
    ]
    """<p>The overrides for the container definition of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskPropertiesOverride) -> dict:
    out: dict = {}
    if "containers" in value:
        import capo_batch.types.list_task_container_overrides

        out["containers"] = (
            capo_batch.types.list_task_container_overrides.serialize_json(
                value["containers"]
            )
        )
    return out


def deserialize_json(data: dict) -> TaskPropertiesOverride:
    out: TaskPropertiesOverride = {}  # type: ignore[typeddict-item]
    if "containers" in data:
        import capo_batch.types.list_task_container_overrides

        out["containers"] = (
            capo_batch.types.list_task_container_overrides.deserialize_json(
                data["containers"]
            )
        )
    return out
