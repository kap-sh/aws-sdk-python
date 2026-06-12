"""Generated from Smithy shape ``com.amazonaws.batch#ListTaskPropertiesOverride``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.task_properties_override

ListTaskPropertiesOverride: TypeAlias = list[
    "aws_sdk_batch.types.task_properties_override.TaskPropertiesOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskPropertiesOverride) -> list:
    import aws_sdk_batch.types.task_properties_override

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.task_properties_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListTaskPropertiesOverride:
    import aws_sdk_batch.types.task_properties_override

    out: ListTaskPropertiesOverride = []
    for item in data:
        out.append(aws_sdk_batch.types.task_properties_override.deserialize_json(item))
    return out
