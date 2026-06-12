"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra_ranking.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.document_list
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_id
    import aws_sdk_kendra_ranking.types.search_query


class RescoreRequest(TypedDict):
    rescore_execution_plan_id: (
        "aws_sdk_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    )
    """<p>The identifier of the rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>"""
    search_query: "aws_sdk_kendra_ranking.types.search_query.SearchQuery"
    """<p>The input query from the search service.</p>"""
    documents: "aws_sdk_kendra_ranking.types.document_list.DocumentList"
    """<p>The list of documents for Amazon Kendra Intelligent Ranking to rescore or rank on.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreRequest) -> dict:
    out: dict = {}
    out["SearchQuery"] = value["search_query"]
    import aws_sdk_kendra_ranking.types.document_list

    out["Documents"] = (
        aws_sdk_kendra_ranking.types.document_list.serialize_aws_json_1_0(
            value["documents"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RescoreRequest:
    out: RescoreRequest = {}  # type: ignore[typeddict-item]
    if "SearchQuery" in data:
        out["search_query"] = data["SearchQuery"]
    else:
        raise DeserializationError("RescoreRequest.search_query required")
    if "Documents" in data:
        import aws_sdk_kendra_ranking.types.document_list

        out["documents"] = (
            aws_sdk_kendra_ranking.types.document_list.deserialize_aws_json_1_0(
                data["Documents"]
            )
        )
    else:
        raise DeserializationError("RescoreRequest.documents required")
    return out
