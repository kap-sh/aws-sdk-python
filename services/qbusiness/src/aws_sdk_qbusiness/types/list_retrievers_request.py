"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListRetrieversRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_retrievers_request
    import aws_sdk_qbusiness.types.next_token


class ListRetrieversRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application using the retriever.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the number of retrievers returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of retrievers.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_retrievers_request.MaxResultsIntegerForListRetrieversRequest"
    ]
    """<p>The maximum number of retrievers returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetrieversRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRetrieversRequest:
    out: ListRetrieversRequest = {}  # type: ignore[typeddict-item]
    return out
