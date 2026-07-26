"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMapperSegmentConstructsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_mapper_segment_constructs
    import capo_mgn.types.pagination_token


class ListNetworkMigrationMapperSegmentConstructsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.network_migration_mapper_segment_constructs.NetworkMigrationMapperSegmentConstructs"
    ]
    """<p>A list of mapper segment constructs.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMapperSegmentConstructsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.network_migration_mapper_segment_constructs

        out["items"] = (
            capo_mgn.types.network_migration_mapper_segment_constructs.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationMapperSegmentConstructsResponse:
    out: ListNetworkMigrationMapperSegmentConstructsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_mgn.types.network_migration_mapper_segment_constructs

        out["items"] = (
            capo_mgn.types.network_migration_mapper_segment_constructs.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
