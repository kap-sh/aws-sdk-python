"""Generated from Smithy shape ``com.amazonaws.ssm#ListDocumentMetadataHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_author
    import aws_sdk_ssm.types.document_metadata_response_info
    import aws_sdk_ssm.types.document_name
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.next_token


class ListDocumentMetadataHistoryResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ssm.types.document_name.DocumentName"]
    """<p>The name of the change template.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the change template.</p>"""
    author: NotRequired["aws_sdk_ssm.types.document_author.DocumentAuthor"]
    """<p>The user ID of the person in the organization who requested the review of the change template.</p>"""
    metadata: NotRequired[
        "aws_sdk_ssm.types.document_metadata_response_info.DocumentMetadataResponseInfo"
    ]
    """<p>Information about the response to the change template approval request.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentMetadataHistoryResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "author" in value:
        out["Author"] = value["author"]
    if "metadata" in value:
        import aws_sdk_ssm.types.document_metadata_response_info

        out["Metadata"] = (
            aws_sdk_ssm.types.document_metadata_response_info.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentMetadataHistoryResponse:
    out: ListDocumentMetadataHistoryResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "Author" in data:
        out["author"] = data["Author"]
    if "Metadata" in data:
        import aws_sdk_ssm.types.document_metadata_response_info

        out["metadata"] = (
            aws_sdk_ssm.types.document_metadata_response_info.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
