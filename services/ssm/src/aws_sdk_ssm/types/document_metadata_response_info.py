"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentMetadataResponseInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_reviewer_response_list


class DocumentMetadataResponseInfo(TypedDict):
    reviewer_response: NotRequired[
        "aws_sdk_ssm.types.document_reviewer_response_list.DocumentReviewerResponseList"
    ]
    """<p>Details about a reviewer's response to a document review request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadataResponseInfo) -> dict:
    out: dict = {}
    if "reviewer_response" in value:
        import aws_sdk_ssm.types.document_reviewer_response_list

        out["ReviewerResponse"] = (
            aws_sdk_ssm.types.document_reviewer_response_list.serialize_aws_json_1_1(
                value["reviewer_response"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentMetadataResponseInfo:
    out: DocumentMetadataResponseInfo = {}  # type: ignore[typeddict-item]
    if "ReviewerResponse" in data:
        import aws_sdk_ssm.types.document_reviewer_response_list

        out["reviewer_response"] = (
            aws_sdk_ssm.types.document_reviewer_response_list.deserialize_aws_json_1_1(
                data["ReviewerResponse"]
            )
        )
    return out
