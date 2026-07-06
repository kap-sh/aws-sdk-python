"""Generated from Smithy shape ``com.amazonaws.kendra#CreateQuerySuggestionsBlockListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.query_suggestions_block_list_id


class CreateQuerySuggestionsBlockListResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId"
    ]
    """<p>The identifier of the block list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateQuerySuggestionsBlockListResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateQuerySuggestionsBlockListResponse:
    out: CreateQuerySuggestionsBlockListResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
