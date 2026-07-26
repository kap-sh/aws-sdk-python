"""Generated from Smithy shape ``com.amazonaws.ssm#ListOpsItemRelatedItemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_related_item_summaries
    import capo_ssm.types.string


class ListOpsItemRelatedItemsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm.types.string.String"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""
    summaries: NotRequired[
        "capo_ssm.types.ops_item_related_item_summaries.OpsItemRelatedItemSummaries"
    ]
    """<p>A list of related-item resources for the specified OpsItem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOpsItemRelatedItemsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "summaries" in value:
        import capo_ssm.types.ops_item_related_item_summaries

        out["Summaries"] = (
            capo_ssm.types.ops_item_related_item_summaries.serialize_aws_json_1_1(
                value["summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOpsItemRelatedItemsResponse:
    out: ListOpsItemRelatedItemsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Summaries" in data:
        import capo_ssm.types.ops_item_related_item_summaries

        out["summaries"] = (
            capo_ssm.types.ops_item_related_item_summaries.deserialize_aws_json_1_1(
                data["Summaries"]
            )
        )
    return out
