"""Generated from Smithy shape ``com.amazonaws.batch#EcsPropertiesDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.list_ecs_task_details


class EcsPropertiesDetail(TypedDict, closed=True):
    task_properties: NotRequired[
        "aws_sdk_batch.types.list_ecs_task_details.ListEcsTaskDetails"
    ]
    """<p>The properties for the Amazon ECS task definition of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsPropertiesDetail) -> dict:
    out: dict = {}
    if "task_properties" in value:
        import aws_sdk_batch.types.list_ecs_task_details

        out["taskProperties"] = (
            aws_sdk_batch.types.list_ecs_task_details.serialize_json(
                value["task_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> EcsPropertiesDetail:
    out: EcsPropertiesDetail = {}  # type: ignore[typeddict-item]
    if "taskProperties" in data:
        import aws_sdk_batch.types.list_ecs_task_details

        out["task_properties"] = (
            aws_sdk_batch.types.list_ecs_task_details.deserialize_json(
                data["taskProperties"]
            )
        )
    return out
