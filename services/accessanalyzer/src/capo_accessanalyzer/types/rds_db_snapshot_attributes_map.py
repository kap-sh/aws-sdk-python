"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbSnapshotAttributesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.rds_db_snapshot_attribute_name
    import capo_accessanalyzer.types.rds_db_snapshot_attribute_value

RdsDbSnapshotAttributesMap: TypeAlias = dict[
    "capo_accessanalyzer.types.rds_db_snapshot_attribute_name.RdsDbSnapshotAttributeName",
    "capo_accessanalyzer.types.rds_db_snapshot_attribute_value.RdsDbSnapshotAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RdsDbSnapshotAttributesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_accessanalyzer.types.rds_db_snapshot_attribute_value

        out[key] = (
            capo_accessanalyzer.types.rds_db_snapshot_attribute_value.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> RdsDbSnapshotAttributesMap:
    out: RdsDbSnapshotAttributesMap = {}
    for key, value in data.items():
        import capo_accessanalyzer.types.rds_db_snapshot_attribute_value

        out[key] = (
            capo_accessanalyzer.types.rds_db_snapshot_attribute_value.deserialize_json(
                value
            )
        )
    return out
