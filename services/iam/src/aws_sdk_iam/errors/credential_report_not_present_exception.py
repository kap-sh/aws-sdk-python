"""Generated from Smithy shape ``com.amazonaws.iam#CredentialReportNotPresentException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.credential_report_not_present_exception_message


class CredentialReportNotPresentException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_iam.types.credential_report_not_present_exception_message.credentialReportNotPresentExceptionMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CredentialReportNotPresentException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> CredentialReportNotPresentException_:
    out: CredentialReportNotPresentException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CredentialReportNotPresentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#CredentialReportNotPresentException``."""

    code: str | None = "CredentialReportNotPresentException"

    def __init__(self, data: CredentialReportNotPresentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CredentialReportNotPresentException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CredentialReportNotPresentException":
        return cls(deserialize_query(el))
