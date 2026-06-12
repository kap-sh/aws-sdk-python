"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssociatedServerIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.string

AssociatedServerIDs: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedServerIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociatedServerIDs:
    return list(data)
