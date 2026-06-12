"""Generated from Smithy shape ``com.amazonaws.memorydb#ReshardingStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.slot_migration


class ReshardingStatus(TypedDict):
    slot_migration: NotRequired["aws_sdk_memorydb.types.slot_migration.SlotMigration"]
    """<p>The status of the online resharding slot migration</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReshardingStatus) -> dict:
    out: dict = {}
    if "slot_migration" in value:
        import aws_sdk_memorydb.types.slot_migration

        out["SlotMigration"] = (
            aws_sdk_memorydb.types.slot_migration.serialize_aws_json_1_1(
                value["slot_migration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReshardingStatus:
    out: ReshardingStatus = {}  # type: ignore[typeddict-item]
    if "SlotMigration" in data:
        import aws_sdk_memorydb.types.slot_migration

        out["slot_migration"] = (
            aws_sdk_memorydb.types.slot_migration.deserialize_aws_json_1_1(
                data["SlotMigration"]
            )
        )
    return out
