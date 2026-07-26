"""Generated from Smithy shape ``com.amazonaws.kendra#QuerySuggestionsBlockListSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.integer
    import capo_kendra.types.query_suggestions_block_list_id
    import capo_kendra.types.query_suggestions_block_list_name
    import capo_kendra.types.query_suggestions_block_list_status
    import capo_kendra.types.timestamp


class QuerySuggestionsBlockListSummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId"
    ]
    """<p>The identifier of a block list.</p>"""
    name: NotRequired[
        "capo_kendra.types.query_suggestions_block_list_name.QuerySuggestionsBlockListName"
    ]
    """<p>The name of the block list.</p>"""
    status: NotRequired[
        "capo_kendra.types.query_suggestions_block_list_status.QuerySuggestionsBlockListStatus"
    ]
    """<p>The status of the block list.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the block list was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the block list was last updated.</p>"""
    item_count: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The number of items in the block list file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuerySuggestionsBlockListSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_kendra.types.query_suggestions_block_list_status

        out["Status"] = (
            capo_kendra.types.query_suggestions_block_list_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra.types.timestamp

        out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QuerySuggestionsBlockListSummary:
    out: QuerySuggestionsBlockListSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import capo_kendra.types.query_suggestions_block_list_status

        out["status"] = (
            capo_kendra.types.query_suggestions_block_list_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreatedAt" in data:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    return out
