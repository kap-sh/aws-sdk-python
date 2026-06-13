"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateConstruct``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.construct_id
    import aws_sdk_mgn.types.network_migration_mapper_segment_construct_type
    import aws_sdk_mgn.types.operation_union
    import aws_sdk_mgn.types.segment_id


class StartNetworkMigrationMappingUpdateConstruct(TypedDict):
    segment_id: "aws_sdk_mgn.types.segment_id.SegmentID"
    """<p>The ID of the segment containing the construct.</p>"""
    construct_id: "aws_sdk_mgn.types.construct_id.ConstructID"
    """<p>The ID of the construct to update.</p>"""
    construct_type: "aws_sdk_mgn.types.network_migration_mapper_segment_construct_type.NetworkMigrationMapperSegmentConstructType"
    """<p>The type of the construct.</p>"""
    operation: NotRequired["aws_sdk_mgn.types.operation_union.OperationUnion"]
    """<p>The operation to perform on the construct.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateConstruct) -> dict:
    out: dict = {}
    out["segmentID"] = value["segment_id"]
    out["constructID"] = value["construct_id"]
    out["constructType"] = value["construct_type"]
    if "operation" in value:
        import aws_sdk_mgn.types.operation_union

        out["operation"] = aws_sdk_mgn.types.operation_union.serialize_json(
            value["operation"]
        )
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationMappingUpdateConstruct:
    out: StartNetworkMigrationMappingUpdateConstruct = {}  # type: ignore[typeddict-item]
    if "segmentID" in data:
        out["segment_id"] = data["segmentID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationMappingUpdateConstruct.segment_id required"
        )
    if "constructID" in data:
        out["construct_id"] = data["constructID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationMappingUpdateConstruct.construct_id required"
        )
    if "constructType" in data:
        out["construct_type"] = data["constructType"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationMappingUpdateConstruct.construct_type required"
        )
    if "operation" in data:
        import aws_sdk_mgn.types.operation_union

        out["operation"] = aws_sdk_mgn.types.operation_union.deserialize_json(
            data["operation"]
        )
    return out
