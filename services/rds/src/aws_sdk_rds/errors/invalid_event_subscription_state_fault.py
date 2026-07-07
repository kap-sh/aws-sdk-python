"""Generated from Smithy shape ``com.amazonaws.rds#InvalidEventSubscriptionStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class InvalidEventSubscriptionStateFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidEventSubscriptionStateFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidEventSubscriptionStateFault_:
    out: InvalidEventSubscriptionStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidEventSubscriptionStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InvalidEventSubscriptionStateFault``."""

    code: str | None = "InvalidEventSubscriptionStateFault"

    def __init__(self, data: InvalidEventSubscriptionStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidEventSubscriptionStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidEventSubscriptionStateFault":
        return cls(deserialize_query(el))
