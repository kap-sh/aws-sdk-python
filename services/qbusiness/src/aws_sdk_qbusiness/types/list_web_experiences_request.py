"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListWebExperiencesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_web_experiences_request
    import aws_sdk_qbusiness.types.next_token


class ListWebExperiencesRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application linked to the listed web experiences.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business conversations.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_web_experiences_request.MaxResultsIntegerForListWebExperiencesRequest"
    ]
    """<p>The maximum number of Amazon Q Business Web Experiences to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebExperiencesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWebExperiencesRequest:
    out: ListWebExperiencesRequest = {}  # type: ignore[typeddict-item]
    return out
