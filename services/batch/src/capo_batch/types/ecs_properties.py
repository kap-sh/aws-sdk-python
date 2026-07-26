"""Generated from Smithy shape ``com.amazonaws.batch#EcsProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.list_ecs_task_properties


class EcsProperties(TypedDict, closed=True):
    task_properties: NotRequired[
        "capo_batch.types.list_ecs_task_properties.ListEcsTaskProperties"
    ]
    """<p>An object that contains the properties for the Amazon ECS task definition of a job.</p> <note> <p>This object is currently limited to one task element. However, the task element can run up to 10 containers.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsProperties) -> dict:
    out: dict = {}
    if "task_properties" in value:
        import capo_batch.types.list_ecs_task_properties

        out["taskProperties"] = (
            capo_batch.types.list_ecs_task_properties.serialize_json(
                value["task_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> EcsProperties:
    out: EcsProperties = {}  # type: ignore[typeddict-item]
    if "taskProperties" in data:
        import capo_batch.types.list_ecs_task_properties

        out["task_properties"] = (
            capo_batch.types.list_ecs_task_properties.deserialize_json(
                data["taskProperties"]
            )
        )
    return out
