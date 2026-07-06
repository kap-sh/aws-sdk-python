"""Generated from Smithy shape ``com.amazonaws.ssm#ListDocumentVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_arn
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token


class ListDocumentVersionsRequest(TypedDict, closed=True):
    name: "aws_sdk_ssm.types.document_arn.DocumentARN"
    """<p>The name of the document. You can specify an Amazon Resource Name (ARN).</p>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentVersionsRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentVersionsRequest:
    out: ListDocumentVersionsRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ListDocumentVersionsRequest.name required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
