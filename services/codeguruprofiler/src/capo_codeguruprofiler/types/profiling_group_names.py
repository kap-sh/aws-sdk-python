"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ProfilingGroupNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.profiling_group_name

ProfilingGroupNames: TypeAlias = list[
    "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfilingGroupNames) -> list:
    return list(value)


def deserialize_json(data: list) -> ProfilingGroupNames:
    return list(data)
