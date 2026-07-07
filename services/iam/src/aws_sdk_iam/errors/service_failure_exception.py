"""Generated from Smithy shape ``com.amazonaws.iam#ServiceFailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.service_failure_exception_message


class ServiceFailureException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_iam.types.service_failure_exception_message.serviceFailureExceptionMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceFailureException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ServiceFailureException_:
    out: ServiceFailureException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ServiceFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#ServiceFailureException``."""

    code: str | None = "ServiceFailureException"

    def __init__(self, data: ServiceFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceFailureException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ServiceFailureException":
        return cls(deserialize_query(el))
