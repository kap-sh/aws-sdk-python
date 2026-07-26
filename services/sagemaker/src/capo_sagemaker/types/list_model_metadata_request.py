"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.model_metadata_search_expression
    import capo_sagemaker.types.next_token


class ListModelMetadataRequest(TypedDict, closed=True):
    search_expression: NotRequired[
        "capo_sagemaker.types.model_metadata_search_expression.ModelMetadataSearchExpression"
    ]
    """<p>One or more filters that searches for the specified resource or resources in a search. All resource objects that satisfy the expression's condition are included in the search results. Specify the Framework, FrameworkVersion, Domain or Task to filter supported. Filter names and values are case-sensitive.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response to a previous <code>ListModelMetadataResponse</code> request was truncated, the response includes a NextToken. To retrieve the next set of model metadata, use the token in the next request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of models to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelMetadataRequest) -> dict:
    out: dict = {}
    if "search_expression" in value:
        import capo_sagemaker.types.model_metadata_search_expression

        out["SearchExpression"] = (
            capo_sagemaker.types.model_metadata_search_expression.serialize_aws_json_1_1(
                value["search_expression"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelMetadataRequest:
    out: ListModelMetadataRequest = {}  # type: ignore[typeddict-item]
    if "SearchExpression" in data:
        import capo_sagemaker.types.model_metadata_search_expression

        out["search_expression"] = (
            capo_sagemaker.types.model_metadata_search_expression.deserialize_aws_json_1_1(
                data["SearchExpression"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
