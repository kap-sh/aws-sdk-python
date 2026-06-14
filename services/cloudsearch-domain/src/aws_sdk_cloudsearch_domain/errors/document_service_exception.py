"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#DocumentServiceException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudsearch_domain.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.string


class DocumentServiceException_(TypedDict):
    status: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    """<p>The return status of a document upload request, <code>error</code> or <code>success</code>.</p>"""
    message: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    """<p>The description of the errors returned by the document service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentServiceException_) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DocumentServiceException_:
    out: DocumentServiceException_ = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DocumentServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudsearchdomain#DocumentServiceException``."""

    code: str | None = "DocumentServiceException"

    def __init__(self, data: DocumentServiceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DocumentServiceException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DocumentServiceException":
        return cls(deserialize_json(data))
