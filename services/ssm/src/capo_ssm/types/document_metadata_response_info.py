"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentMetadataResponseInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_reviewer_response_list


class DocumentMetadataResponseInfo(TypedDict, closed=True):
    reviewer_response: NotRequired[
        "capo_ssm.types.document_reviewer_response_list.DocumentReviewerResponseList"
    ]
    """<p>Details about a reviewer's response to a document review request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadataResponseInfo) -> dict:
    out: dict = {}
    if "reviewer_response" in value:
        import capo_ssm.types.document_reviewer_response_list

        out["ReviewerResponse"] = (
            capo_ssm.types.document_reviewer_response_list.serialize_aws_json_1_1(
                value["reviewer_response"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentMetadataResponseInfo:
    out: DocumentMetadataResponseInfo = {}  # type: ignore[typeddict-item]
    if data.get("ReviewerResponse") is not None:
        import capo_ssm.types.document_reviewer_response_list

        out["reviewer_response"] = (
            capo_ssm.types.document_reviewer_response_list.deserialize_aws_json_1_1(
                data["ReviewerResponse"]
            )
        )
    return out
