"""Generated from Smithy shape ``com.amazonaws.backup#ConditionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.condition_parameter

ConditionParameters: TypeAlias = list[
    "capo_backup.types.condition_parameter.ConditionParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionParameters) -> list:
    import capo_backup.types.condition_parameter

    out: list = []
    for item in value:
        out.append(capo_backup.types.condition_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConditionParameters:
    import capo_backup.types.condition_parameter

    out: ConditionParameters = []
    for item in data:
        out.append(capo_backup.types.condition_parameter.deserialize_json(item))
    return out
