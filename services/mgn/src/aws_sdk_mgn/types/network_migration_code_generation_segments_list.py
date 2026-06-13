"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationCodeGenerationSegmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_code_generation_segment

NetworkMigrationCodeGenerationSegmentsList: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_code_generation_segment.NetworkMigrationCodeGenerationSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationCodeGenerationSegmentsList) -> list:
    import aws_sdk_mgn.types.network_migration_code_generation_segment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.network_migration_code_generation_segment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationCodeGenerationSegmentsList:
    import aws_sdk_mgn.types.network_migration_code_generation_segment

    out: NetworkMigrationCodeGenerationSegmentsList = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.network_migration_code_generation_segment.deserialize_json(
                item
            )
        )
    return out
