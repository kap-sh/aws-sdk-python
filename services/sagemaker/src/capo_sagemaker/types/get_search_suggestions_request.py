"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetSearchSuggestionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.resource_type
    import capo_sagemaker.types.suggestion_query


class GetSearchSuggestionsRequest(TypedDict, closed=True):
    resource: NotRequired["capo_sagemaker.types.resource_type.ResourceType"]
    """<p>The name of the SageMaker resource to search for.</p>"""
    suggestion_query: NotRequired[
        "capo_sagemaker.types.suggestion_query.SuggestionQuery"
    ]
    """<p>Limits the property names that are included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSearchSuggestionsRequest) -> dict:
    out: dict = {}
    if "resource" in value:
        import capo_sagemaker.types.resource_type

        out["Resource"] = capo_sagemaker.types.resource_type.serialize_aws_json_1_1(
            value["resource"]
        )
    if "suggestion_query" in value:
        import capo_sagemaker.types.suggestion_query

        out["SuggestionQuery"] = (
            capo_sagemaker.types.suggestion_query.serialize_aws_json_1_1(
                value["suggestion_query"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSearchSuggestionsRequest:
    out: GetSearchSuggestionsRequest = {}  # type: ignore[typeddict-item]
    if "Resource" in data:
        import capo_sagemaker.types.resource_type

        out["resource"] = capo_sagemaker.types.resource_type.deserialize_aws_json_1_1(
            data["Resource"]
        )
    if "SuggestionQuery" in data:
        import capo_sagemaker.types.suggestion_query

        out["suggestion_query"] = (
            capo_sagemaker.types.suggestion_query.deserialize_aws_json_1_1(
                data["SuggestionQuery"]
            )
        )
    return out
