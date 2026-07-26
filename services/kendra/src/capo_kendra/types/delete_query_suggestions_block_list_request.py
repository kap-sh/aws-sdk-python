"""Generated from Smithy shape ``com.amazonaws.kendra#DeleteQuerySuggestionsBlockListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.index_id
    import capo_kendra.types.query_suggestions_block_list_id


class DeleteQuerySuggestionsBlockListRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the block list.</p>"""
    id: "capo_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId"
    """<p>The identifier of the block list you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteQuerySuggestionsBlockListRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteQuerySuggestionsBlockListRequest:
    out: DeleteQuerySuggestionsBlockListRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "DeleteQuerySuggestionsBlockListRequest.index_id required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteQuerySuggestionsBlockListRequest.id required")
    return out
