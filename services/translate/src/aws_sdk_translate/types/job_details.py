"""Generated from Smithy shape ``com.amazonaws.translate#JobDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_translate.types.integer


class JobDetails(TypedDict):
    translated_documents_count: NotRequired["aws_sdk_translate.types.integer.Integer"]
    """<p>The number of documents successfully processed during a translation job.</p>"""
    documents_with_errors_count: NotRequired["aws_sdk_translate.types.integer.Integer"]
    """<p>The number of documents that could not be processed during a translation job.</p>"""
    input_documents_count: NotRequired["aws_sdk_translate.types.integer.Integer"]
    """<p>The number of documents used as input in a translation job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobDetails) -> dict:
    out: dict = {}
    if "translated_documents_count" in value:
        out["TranslatedDocumentsCount"] = value["translated_documents_count"]
    if "documents_with_errors_count" in value:
        out["DocumentsWithErrorsCount"] = value["documents_with_errors_count"]
    if "input_documents_count" in value:
        out["InputDocumentsCount"] = value["input_documents_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobDetails:
    out: JobDetails = {}  # type: ignore[typeddict-item]
    if "TranslatedDocumentsCount" in data:
        out["translated_documents_count"] = data["TranslatedDocumentsCount"]
    if "DocumentsWithErrorsCount" in data:
        out["documents_with_errors_count"] = data["DocumentsWithErrorsCount"]
    if "InputDocumentsCount" in data:
        out["input_documents_count"] = data["InputDocumentsCount"]
    return out
