"""Generated from Smithy shape ``com.amazonaws.bedrock#ListProvisionedModelThroughputsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.provisioned_model_summaries


class ListProvisionedModelThroughputsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>If there are more results than the number you specified in the <code>maxResults</code> field, this value is returned. To see the next batch of results, include this value in the <code>nextToken</code> field in another list request.</p>"""
    provisioned_model_summaries: NotRequired[
        "capo_bedrock.types.provisioned_model_summaries.ProvisionedModelSummaries"
    ]
    """<p>A list of summaries, one for each Provisioned Throughput in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisionedModelThroughputsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "provisioned_model_summaries" in value:
        import capo_bedrock.types.provisioned_model_summaries

        out["provisionedModelSummaries"] = (
            capo_bedrock.types.provisioned_model_summaries.serialize_json(
                value["provisioned_model_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListProvisionedModelThroughputsResponse:
    out: ListProvisionedModelThroughputsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("provisionedModelSummaries") is not None:
        import capo_bedrock.types.provisioned_model_summaries

        out["provisioned_model_summaries"] = (
            capo_bedrock.types.provisioned_model_summaries.deserialize_json(
                data["provisionedModelSummaries"]
            )
        )
    return out
