"""Generated from Smithy shape ``com.amazonaws.emrserverless#EntryPointArguments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_serverless.types.entry_point_argument

EntryPointArguments: TypeAlias = list[
    "capo_emr_serverless.types.entry_point_argument.EntryPointArgument"
]


# --- restJson1 ser/de ---
def serialize_json(value: EntryPointArguments) -> list:
    return list(value)


def deserialize_json(data: list) -> EntryPointArguments:
    return list(data)
