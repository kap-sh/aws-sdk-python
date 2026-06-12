"""Generated from Smithy shape ``com.amazonaws.emrcontainers#EntryPointArguments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.entry_point_argument

EntryPointArguments: TypeAlias = list[
    "aws_sdk_emr_containers.types.entry_point_argument.EntryPointArgument"
]


# --- restJson1 ser/de ---
def serialize_json(value: EntryPointArguments) -> list:
    return list(value)


def deserialize_json(data: list) -> EntryPointArguments:
    return list(data)
