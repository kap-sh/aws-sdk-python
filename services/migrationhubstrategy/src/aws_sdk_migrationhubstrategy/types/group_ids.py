"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.group

GroupIds: TypeAlias = list["aws_sdk_migrationhubstrategy.types.group.Group"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupIds) -> list:
    import aws_sdk_migrationhubstrategy.types.group

    out: list = []
    for item in value:
        out.append(aws_sdk_migrationhubstrategy.types.group.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupIds:
    import aws_sdk_migrationhubstrategy.types.group

    out: GroupIds = []
    for item in data:
        out.append(aws_sdk_migrationhubstrategy.types.group.deserialize_json(item))
    return out
