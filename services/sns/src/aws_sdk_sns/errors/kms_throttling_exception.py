"""Generated from Smithy shape ``com.amazonaws.sns#KMSThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class KMSThrottlingException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sns.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: KMSThrottlingException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> KMSThrottlingException_:
    out: KMSThrottlingException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class KMSThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sns#KMSThrottlingException``."""

    code: str | None = "KMSThrottlingException"

    def __init__(self, data: KMSThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSThrottlingException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "KMSThrottlingException":
        return cls(deserialize_query(el))
