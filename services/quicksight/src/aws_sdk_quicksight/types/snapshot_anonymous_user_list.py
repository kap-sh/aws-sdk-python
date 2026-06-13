"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotAnonymousUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_anonymous_user

SnapshotAnonymousUserList: TypeAlias = list[
    "aws_sdk_quicksight.types.snapshot_anonymous_user.SnapshotAnonymousUser"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotAnonymousUserList) -> list:
    import aws_sdk_quicksight.types.snapshot_anonymous_user

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.snapshot_anonymous_user.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SnapshotAnonymousUserList:
    import aws_sdk_quicksight.types.snapshot_anonymous_user

    out: SnapshotAnonymousUserList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.snapshot_anonymous_user.deserialize_json(item)
        )
    return out
