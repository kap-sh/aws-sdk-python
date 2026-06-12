"""Generated from Smithy shape ``com.amazonaws.batch#EcsPropertiesOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.list_task_properties_override


class EcsPropertiesOverride(TypedDict):
    task_properties: NotRequired[
        "aws_sdk_batch.types.list_task_properties_override.ListTaskPropertiesOverride"
    ]
    """<p>The overrides for the Amazon ECS task definition of a job.</p> <note> <p>This object is currently limited to one element.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsPropertiesOverride) -> dict:
    out: dict = {}
    if "task_properties" in value:
        import aws_sdk_batch.types.list_task_properties_override

        out["taskProperties"] = (
            aws_sdk_batch.types.list_task_properties_override.serialize_json(
                value["task_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> EcsPropertiesOverride:
    out: EcsPropertiesOverride = {}  # type: ignore[typeddict-item]
    if "taskProperties" in data:
        import aws_sdk_batch.types.list_task_properties_override

        out["task_properties"] = (
            aws_sdk_batch.types.list_task_properties_override.deserialize_json(
                data["taskProperties"]
            )
        )
    return out
