"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingSelections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_selection_for_list

RestoreTestingSelections: TypeAlias = list[
    "capo_backup.types.restore_testing_selection_for_list.RestoreTestingSelectionForList"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingSelections) -> list:
    import capo_backup.types.restore_testing_selection_for_list

    out: list = []
    for item in value:
        out.append(
            capo_backup.types.restore_testing_selection_for_list.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RestoreTestingSelections:
    import capo_backup.types.restore_testing_selection_for_list

    out: RestoreTestingSelections = []
    for item in data:
        out.append(
            capo_backup.types.restore_testing_selection_for_list.deserialize_json(item)
        )
    return out
