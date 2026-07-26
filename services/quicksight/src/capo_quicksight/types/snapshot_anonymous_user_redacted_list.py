"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotAnonymousUserRedactedList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_anonymous_user_redacted

SnapshotAnonymousUserRedactedList: TypeAlias = list[
    "capo_quicksight.types.snapshot_anonymous_user_redacted.SnapshotAnonymousUserRedacted"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotAnonymousUserRedactedList) -> list:
    import capo_quicksight.types.snapshot_anonymous_user_redacted

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.snapshot_anonymous_user_redacted.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SnapshotAnonymousUserRedactedList:
    import capo_quicksight.types.snapshot_anonymous_user_redacted

    out: SnapshotAnonymousUserRedactedList = []
    for item in data:
        out.append(
            capo_quicksight.types.snapshot_anonymous_user_redacted.deserialize_json(
                item
            )
        )
    return out
