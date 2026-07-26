"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.string_list_member

StringList: TypeAlias = list[
    "capo_migrationhuborchestrator.types.string_list_member.StringListMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return list(data)
