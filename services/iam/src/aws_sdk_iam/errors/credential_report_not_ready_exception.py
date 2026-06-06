"""Generated from Smithy shape ``com.amazonaws.iam#CredentialReportNotReadyException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.credential_report_not_ready_exception_message


class CredentialReportNotReadyException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.credential_report_not_ready_exception_message.credentialReportNotReadyExceptionMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CredentialReportNotReadyException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> CredentialReportNotReadyException_:
    out: CredentialReportNotReadyException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CredentialReportNotReadyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#CredentialReportNotReadyException``."""

    code: str | None = "CredentialReportNotReadyException"

    def __init__(self, data: CredentialReportNotReadyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CredentialReportNotReadyException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CredentialReportNotReadyException":
        return cls(deserialize_query(el))
