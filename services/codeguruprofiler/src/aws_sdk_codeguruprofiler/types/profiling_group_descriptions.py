"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ProfilingGroupDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.profiling_group_description

ProfilingGroupDescriptions: TypeAlias = list[
    "aws_sdk_codeguruprofiler.types.profiling_group_description.ProfilingGroupDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfilingGroupDescriptions) -> list:
    import aws_sdk_codeguruprofiler.types.profiling_group_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguruprofiler.types.profiling_group_description.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProfilingGroupDescriptions:
    import aws_sdk_codeguruprofiler.types.profiling_group_description

    out: ProfilingGroupDescriptions = []
    for item in data:
        out.append(
            aws_sdk_codeguruprofiler.types.profiling_group_description.deserialize_json(
                item
            )
        )
    return out
