"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMapperSegmentConstruct``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.construct_id
    import capo_mgn.types.construct_properties
    import capo_mgn.types.logical_id
    import capo_mgn.types.network_migration_mapper_segment_construct_type
    import capo_mgn.types.segment_construct_description
    import capo_mgn.types.segment_construct_name


class NetworkMigrationMapperSegmentConstruct(TypedDict, closed=True):
    construct_id: NotRequired["capo_mgn.types.construct_id.ConstructID"]
    """<p>The unique identifier of the construct.</p>"""
    construct_type: NotRequired[
        "capo_mgn.types.network_migration_mapper_segment_construct_type.NetworkMigrationMapperSegmentConstructType"
    ]
    """<p>The type of the construct, such as VPC, subnet, security group, or route table.</p>"""
    name: NotRequired["capo_mgn.types.segment_construct_name.SegmentConstructName"]
    """<p>The name of the construct.</p>"""
    description: NotRequired[
        "capo_mgn.types.segment_construct_description.SegmentConstructDescription"
    ]
    """<p>A description of the construct.</p>"""
    logical_id: NotRequired["capo_mgn.types.logical_id.LogicalID"]
    """<p>The logical identifier for the construct in the infrastructure code.</p>"""
    excluded: NotRequired["bool"]
    """<p>Whether this construct is excluded from the migration.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the construct was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the construct was last updated.</p>"""
    properties: NotRequired["capo_mgn.types.construct_properties.ConstructProperties"]
    """<p>The properties and configuration of the construct.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMapperSegmentConstruct) -> dict:
    out: dict = {}
    if "construct_id" in value:
        out["constructID"] = value["construct_id"]
    if "construct_type" in value:
        out["constructType"] = value["construct_type"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "logical_id" in value:
        out["logicalID"] = value["logical_id"]
    if "excluded" in value:
        out["excluded"] = value["excluded"]
    if "created_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["createdAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["updatedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "properties" in value:
        import capo_mgn.types.construct_properties

        out["properties"] = capo_mgn.types.construct_properties.serialize_json(
            value["properties"]
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationMapperSegmentConstruct:
    out: NetworkMigrationMapperSegmentConstruct = {}  # type: ignore[typeddict-item]
    if "constructID" in data:
        out["construct_id"] = data["constructID"]
    if "constructType" in data:
        out["construct_type"] = data["constructType"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "logicalID" in data:
        out["logical_id"] = data["logicalID"]
    if "excluded" in data:
        out["excluded"] = data["excluded"]
    if "createdAt" in data:
        import capo_mgn.types._prelude.timestamp

        out["created_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_mgn.types._prelude.timestamp

        out["updated_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "properties" in data:
        import capo_mgn.types.construct_properties

        out["properties"] = capo_mgn.types.construct_properties.deserialize_json(
            data["properties"]
        )
    return out
