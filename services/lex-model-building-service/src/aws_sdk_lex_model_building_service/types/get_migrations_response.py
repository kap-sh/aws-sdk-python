"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetMigrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.migration_summary_list
    import aws_sdk_lex_model_building_service.types.next_token


class GetMigrationsResponse(TypedDict, closed=True):
    migration_summaries: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_summary_list.MigrationSummaryList"
    ]
    """<p>An array of summaries for migrations from Amazon Lex V1 to Amazon Lex V2. To see details of the migration, use the <code>migrationId</code> from the summary in a call to the operation.</p>"""
    next_token: NotRequired[
        "aws_sdk_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>If the response is truncated, it includes a pagination token that you can specify in your next request to fetch the next page of migrations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationsResponse) -> dict:
    out: dict = {}
    if "migration_summaries" in value:
        import aws_sdk_lex_model_building_service.types.migration_summary_list

        out["migrationSummaries"] = (
            aws_sdk_lex_model_building_service.types.migration_summary_list.serialize_json(
                value["migration_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetMigrationsResponse:
    out: GetMigrationsResponse = {}  # type: ignore[typeddict-item]
    if "migrationSummaries" in data:
        import aws_sdk_lex_model_building_service.types.migration_summary_list

        out["migration_summaries"] = (
            aws_sdk_lex_model_building_service.types.migration_summary_list.deserialize_json(
                data["migrationSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
