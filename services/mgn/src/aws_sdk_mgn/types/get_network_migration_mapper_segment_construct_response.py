"""Generated from Smithy shape ``com.amazonaws.mgn#GetNetworkMigrationMapperSegmentConstructResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_mapper_segment_construct


class GetNetworkMigrationMapperSegmentConstructResponse(TypedDict, closed=True):
    construct: NotRequired[
        "aws_sdk_mgn.types.network_migration_mapper_segment_construct.NetworkMigrationMapperSegmentConstruct"
    ]
    """<p>The construct metadata including type, name, and configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkMigrationMapperSegmentConstructResponse) -> dict:
    out: dict = {}
    if "construct" in value:
        import aws_sdk_mgn.types.network_migration_mapper_segment_construct

        out["construct"] = (
            aws_sdk_mgn.types.network_migration_mapper_segment_construct.serialize_json(
                value["construct"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetNetworkMigrationMapperSegmentConstructResponse:
    out: GetNetworkMigrationMapperSegmentConstructResponse = {}  # type: ignore[typeddict-item]
    if "construct" in data:
        import aws_sdk_mgn.types.network_migration_mapper_segment_construct

        out["construct"] = (
            aws_sdk_mgn.types.network_migration_mapper_segment_construct.deserialize_json(
                data["construct"]
            )
        )
    return out
