"""Generated from Smithy shape ``com.amazonaws.bedrock#ListInferenceProfilesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.inference_profile_type
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.pagination_token


class ListInferenceProfilesRequest(TypedDict):
    max_results: NotRequired["aws_sdk_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    type_equals: NotRequired[
        "aws_sdk_bedrock.types.inference_profile_type.InferenceProfileType"
    ]
    """<p>Filters for inference profiles that match the type you specify.</p> <ul> <li> <p> <code>SYSTEM_DEFINED</code> – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.</p> </li> <li> <p> <code>APPLICATION</code> – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInferenceProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInferenceProfilesRequest:
    out: ListInferenceProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
