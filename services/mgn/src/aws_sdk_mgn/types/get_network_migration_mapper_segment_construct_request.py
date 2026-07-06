"""Generated from Smithy shape ``com.amazonaws.mgn#GetNetworkMigrationMapperSegmentConstructRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.construct_id
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.segment_id


class GetNetworkMigrationMapperSegmentConstructRequest(TypedDict, closed=True):
    network_migration_definition_id: (
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    network_migration_execution_id: (
        "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    segment_id: "aws_sdk_mgn.types.segment_id.SegmentID"
    """<p>The unique identifier of the mapper segment.</p>"""
    construct_id: "aws_sdk_mgn.types.construct_id.ConstructID"
    """<p>The unique identifier of the construct within the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkMigrationMapperSegmentConstructRequest) -> dict:
    out: dict = {}
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["segmentID"] = value["segment_id"]
    out["constructID"] = value["construct_id"]
    return out


def deserialize_json(data: dict) -> GetNetworkMigrationMapperSegmentConstructRequest:
    out: GetNetworkMigrationMapperSegmentConstructRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "GetNetworkMigrationMapperSegmentConstructRequest.network_migration_definition_id required"
        )
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        raise DeserializationError(
            "GetNetworkMigrationMapperSegmentConstructRequest.network_migration_execution_id required"
        )
    if "segmentID" in data:
        out["segment_id"] = data["segmentID"]
    else:
        raise DeserializationError(
            "GetNetworkMigrationMapperSegmentConstructRequest.segment_id required"
        )
    if "constructID" in data:
        out["construct_id"] = data["constructID"]
    else:
        raise DeserializationError(
            "GetNetworkMigrationMapperSegmentConstructRequest.construct_id required"
        )
    return out
