"""Generated from Smithy shape ``com.amazonaws.iam#CredentialReportExpiredException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.credential_report_expired_exception_message


class CredentialReportExpiredException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.credential_report_expired_exception_message.credentialReportExpiredExceptionMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CredentialReportExpiredException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> CredentialReportExpiredException_:
    out: CredentialReportExpiredException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CredentialReportExpiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#CredentialReportExpiredException``."""

    code: str | None = "CredentialReportExpiredException"

    def __init__(self, data: CredentialReportExpiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CredentialReportExpiredException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CredentialReportExpiredException":
        return cls(deserialize_query(el))
