"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbSnapshotAttributesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.rds_db_snapshot_attribute_name
    import aws_sdk_accessanalyzer.types.rds_db_snapshot_attribute_value

RdsDbSnapshotAttributesMap: TypeAlias = dict[
    "aws_sdk_accessanalyzer.types.rds_db_snapshot_attribute_name.RdsDbSnapshotAttributeName",
    "aws_sdk_accessanalyzer.types.rds_db_snapshot_attribute_value.RdsDbSnapshotAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RdsDbSnapshotAttributesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_accessanalyzer.types.rds_db_snapshot_attribute_value

        out[key] = (
            aws_sdk_accessanalyzer.types.rds_db_snapshot_attribute_value.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> RdsDbSnapshotAttributesMap:
    out: RdsDbSnapshotAttributesMap = {}
    for key, value in data.items():
        import aws_sdk_accessanalyzer.types.rds_db_snapshot_attribute_value

        out[key] = (
            aws_sdk_accessanalyzer.types.rds_db_snapshot_attribute_value.deserialize_json(
                value
            )
        )
    return out
