"""Generated from Smithy shape ``com.amazonaws.kendra#Status``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_id
    import aws_sdk_kendra.types.document_status
    import aws_sdk_kendra.types.string


class Status(TypedDict, closed=True):
    document_id: NotRequired["aws_sdk_kendra.types.document_id.DocumentId"]
    """<p>The identifier of the document.</p>"""
    document_status: NotRequired["aws_sdk_kendra.types.document_status.DocumentStatus"]
    """<p>The current status of a document.</p> <p>If the document was submitted for deletion, the status is <code>NOT_FOUND</code> after the document is deleted.</p>"""
    failure_code: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>Indicates the source of the error.</p>"""
    failure_reason: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>Provides detailed information about why the document couldn't be indexed. Use this information to correct the error before you resubmit the document for indexing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Status) -> dict:
    out: dict = {}
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "document_status" in value:
        import aws_sdk_kendra.types.document_status

        out["DocumentStatus"] = (
            aws_sdk_kendra.types.document_status.serialize_aws_json_1_1(
                value["document_status"]
            )
        )
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Status:
    out: Status = {}  # type: ignore[typeddict-item]
    if "DocumentId" in data:
        out["document_id"] = data["DocumentId"]
    if "DocumentStatus" in data:
        import aws_sdk_kendra.types.document_status

        out["document_status"] = (
            aws_sdk_kendra.types.document_status.deserialize_aws_json_1_1(
                data["DocumentStatus"]
            )
        )
    if "FailureCode" in data:
        out["failure_code"] = data["FailureCode"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
