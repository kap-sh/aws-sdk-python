"""Generated from Smithy shape ``com.amazonaws.ssm#ListDocumentMetadataHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_metadata_enum
    import aws_sdk_ssm.types.document_name
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token


class ListDocumentMetadataHistoryRequest(TypedDict, closed=True):
    name: "aws_sdk_ssm.types.document_name.DocumentName"
    """<p>The name of the change template.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the change template.</p>"""
    metadata: "aws_sdk_ssm.types.document_metadata_enum.DocumentMetadataEnum"
    """<p>The type of data for which details are being requested. Currently, the only supported value is <code>DocumentReviews</code>.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentMetadataHistoryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    import aws_sdk_ssm.types.document_metadata_enum

    out["Metadata"] = aws_sdk_ssm.types.document_metadata_enum.serialize_aws_json_1_1(
        value["metadata"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentMetadataHistoryRequest:
    out: ListDocumentMetadataHistoryRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ListDocumentMetadataHistoryRequest.name required")
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "Metadata" in data:
        import aws_sdk_ssm.types.document_metadata_enum

        out["metadata"] = (
            aws_sdk_ssm.types.document_metadata_enum.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    else:
        raise DeserializationError(
            "ListDocumentMetadataHistoryRequest.metadata required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
