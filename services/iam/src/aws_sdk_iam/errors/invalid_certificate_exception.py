"""Generated from Smithy shape ``com.amazonaws.iam#InvalidCertificateException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.invalid_certificate_message


class InvalidCertificateException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.invalid_certificate_message.invalidCertificateMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidCertificateException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidCertificateException_:
    out: InvalidCertificateException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidCertificateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#InvalidCertificateException``."""

    code: str | None = "InvalidCertificateException"

    def __init__(self, data: InvalidCertificateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCertificateException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidCertificateException":
        return cls(deserialize_query(el))
