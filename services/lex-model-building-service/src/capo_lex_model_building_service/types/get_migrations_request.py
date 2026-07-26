"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetMigrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.max_results
    import capo_lex_model_building_service.types.migration_sort_attribute
    import capo_lex_model_building_service.types.migration_status
    import capo_lex_model_building_service.types.next_token
    import capo_lex_model_building_service.types.sort_order


class GetMigrationsRequest(TypedDict, closed=True):
    sort_by_attribute: NotRequired[
        "capo_lex_model_building_service.types.migration_sort_attribute.MigrationSortAttribute"
    ]
    """<p>The field to sort the list of migrations by. You can sort by the Amazon Lex V1 bot name or the date and time that the migration was started.</p>"""
    sort_by_order: NotRequired[
        "capo_lex_model_building_service.types.sort_order.SortOrder"
    ]
    """<p>The order so sort the list.</p>"""
    v1_bot_name_contains: NotRequired[
        "capo_lex_model_building_service.types.bot_name.BotName"
    ]
    """<p>Filters the list to contain only bots whose name contains the specified string. The string is matched anywhere in bot name.</p>"""
    migration_status_equals: NotRequired[
        "capo_lex_model_building_service.types.migration_status.MigrationStatus"
    ]
    """<p>Filters the list to contain only migrations in the specified state.</p>"""
    max_results: NotRequired[
        "capo_lex_model_building_service.types.max_results.MaxResults"
    ]
    """<p>The maximum number of migrations to return in the response. The default is 10.</p>"""
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token that fetches the next page of migrations. If the response to this operation is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of migrations, specify the pagination token in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMigrationsRequest:
    out: GetMigrationsRequest = {}  # type: ignore[typeddict-item]
    return out
