"""Generated from Smithy shape ``com.amazonaws.rds#EventSubscriptionQuotaExceededFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class EventSubscriptionQuotaExceededFault_(TypedDict):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventSubscriptionQuotaExceededFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> EventSubscriptionQuotaExceededFault_:
    out: EventSubscriptionQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class EventSubscriptionQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#EventSubscriptionQuotaExceededFault``."""

    code: str | None = "EventSubscriptionQuotaExceededFault"

    def __init__(self, data: EventSubscriptionQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EventSubscriptionQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "EventSubscriptionQuotaExceededFault":
        return cls(deserialize_query(el))
