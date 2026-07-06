"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetSearchSuggestionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.resource_type
    import aws_sdk_sagemaker.types.suggestion_query


class GetSearchSuggestionsRequest(TypedDict, closed=True):
    resource: NotRequired["aws_sdk_sagemaker.types.resource_type.ResourceType"]
    """<p>The name of the SageMaker resource to search for.</p>"""
    suggestion_query: NotRequired[
        "aws_sdk_sagemaker.types.suggestion_query.SuggestionQuery"
    ]
    """<p>Limits the property names that are included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSearchSuggestionsRequest) -> dict:
    out: dict = {}
    if "resource" in value:
        import aws_sdk_sagemaker.types.resource_type

        out["Resource"] = aws_sdk_sagemaker.types.resource_type.serialize_aws_json_1_1(
            value["resource"]
        )
    if "suggestion_query" in value:
        import aws_sdk_sagemaker.types.suggestion_query

        out["SuggestionQuery"] = (
            aws_sdk_sagemaker.types.suggestion_query.serialize_aws_json_1_1(
                value["suggestion_query"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSearchSuggestionsRequest:
    out: GetSearchSuggestionsRequest = {}  # type: ignore[typeddict-item]
    if "Resource" in data:
        import aws_sdk_sagemaker.types.resource_type

        out["resource"] = (
            aws_sdk_sagemaker.types.resource_type.deserialize_aws_json_1_1(
                data["Resource"]
            )
        )
    if "SuggestionQuery" in data:
        import aws_sdk_sagemaker.types.suggestion_query

        out["suggestion_query"] = (
            aws_sdk_sagemaker.types.suggestion_query.deserialize_aws_json_1_1(
                data["SuggestionQuery"]
            )
        )
    return out
