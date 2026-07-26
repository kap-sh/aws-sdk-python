"""Generated from Smithy shape ``com.amazonaws.batch#ListTaskPropertiesOverride``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.task_properties_override

ListTaskPropertiesOverride: TypeAlias = list[
    "capo_batch.types.task_properties_override.TaskPropertiesOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskPropertiesOverride) -> list:
    import capo_batch.types.task_properties_override

    out: list = []
    for item in value:
        out.append(capo_batch.types.task_properties_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListTaskPropertiesOverride:
    import capo_batch.types.task_properties_override

    out: ListTaskPropertiesOverride = []
    for item in data:
        out.append(capo_batch.types.task_properties_override.deserialize_json(item))
    return out
