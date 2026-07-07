"""Generated from Smithy shape ``com.amazonaws.kendra#QuerySuggestionsBlockListSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.integer
    import aws_sdk_kendra.types.query_suggestions_block_list_id
    import aws_sdk_kendra.types.query_suggestions_block_list_name
    import aws_sdk_kendra.types.query_suggestions_block_list_status
    import aws_sdk_kendra.types.timestamp


class QuerySuggestionsBlockListSummary(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId"
    ]
    """<p>The identifier of a block list.</p>"""
    name: NotRequired[
        "aws_sdk_kendra.types.query_suggestions_block_list_name.QuerySuggestionsBlockListName"
    ]
    """<p>The name of the block list.</p>"""
    status: NotRequired[
        "aws_sdk_kendra.types.query_suggestions_block_list_status.QuerySuggestionsBlockListStatus"
    ]
    """<p>The status of the block list.</p>"""
    created_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the block list was created.</p>"""
    updated_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the block list was last updated.</p>"""
    item_count: NotRequired["aws_sdk_kendra.types.integer.Integer"]
    """<p>The number of items in the block list file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuerySuggestionsBlockListSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_kendra.types.query_suggestions_block_list_status

        out["Status"] = (
            aws_sdk_kendra.types.query_suggestions_block_list_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["CreatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["UpdatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
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
        import aws_sdk_kendra.types.query_suggestions_block_list_status

        out["status"] = (
            aws_sdk_kendra.types.query_suggestions_block_list_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["created_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["updated_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    return out
