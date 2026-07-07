"""Generated from Smithy shape ``com.amazonaws.docdb#SubscriptionNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element
from aws_sdk_docdb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_docdb.types.exception_message


class SubscriptionNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_docdb.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SubscriptionNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> SubscriptionNotFoundFault_:
    out: SubscriptionNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class SubscriptionNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.docdb#SubscriptionNotFoundFault``."""

    code: str | None = "SubscriptionNotFoundFault"

    def __init__(self, data: SubscriptionNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SubscriptionNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "SubscriptionNotFoundFault":
        return cls(deserialize_query(el))
