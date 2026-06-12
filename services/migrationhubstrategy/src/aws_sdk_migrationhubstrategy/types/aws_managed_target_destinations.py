"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AwsManagedTargetDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.aws_managed_target_destination

AwsManagedTargetDestinations: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.aws_managed_target_destination.AwsManagedTargetDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsManagedTargetDestinations) -> list:
    return list(value)


def deserialize_json(data: list) -> AwsManagedTargetDestinations:
    return list(data)
