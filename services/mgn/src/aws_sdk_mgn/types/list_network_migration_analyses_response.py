"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationAnalysesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_analyses_list
    import aws_sdk_mgn.types.pagination_token


class ListNetworkMigrationAnalysesResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_mgn.types.network_migration_analyses_list.NetworkMigrationAnalysesList"
    ]
    """<p>A list of network migration analysis job details.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationAnalysesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mgn.types.network_migration_analyses_list

        out["items"] = aws_sdk_mgn.types.network_migration_analyses_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationAnalysesResponse:
    out: ListNetworkMigrationAnalysesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_mgn.types.network_migration_analyses_list

        out["items"] = (
            aws_sdk_mgn.types.network_migration_analyses_list.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
