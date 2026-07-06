"""Generated from Smithy shape ``com.amazonaws.iam#ServiceNotSupportedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.service_not_supported_message


class ServiceNotSupportedException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_iam.types.service_not_supported_message.serviceNotSupportedMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceNotSupportedException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ServiceNotSupportedException_:
    out: ServiceNotSupportedException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ServiceNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#ServiceNotSupportedException``."""

    code: str | None = "ServiceNotSupportedException"

    def __init__(self, data: ServiceNotSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceNotSupportedException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ServiceNotSupportedException":
        return cls(deserialize_query(el))
