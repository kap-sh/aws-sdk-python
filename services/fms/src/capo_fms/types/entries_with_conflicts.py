"""Generated from Smithy shape ``com.amazonaws.fms#EntriesWithConflicts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.entry_description

EntriesWithConflicts: TypeAlias = list[
    "capo_fms.types.entry_description.EntryDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntriesWithConflicts) -> list:
    import capo_fms.types.entry_description

    out: list = []
    for item in value:
        out.append(capo_fms.types.entry_description.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntriesWithConflicts:
    import capo_fms.types.entry_description

    out: EntriesWithConflicts = []
    for item in data:
        out.append(capo_fms.types.entry_description.deserialize_aws_json_1_1(item))
    return out
