"""Generated from Smithy shape ``com.amazonaws.sns#SubscriptionLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import ServiceError

if TYPE_CHECKING:
    import capo_sns.types.string


class SubscriptionLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_sns.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SubscriptionLimitExceededException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> SubscriptionLimitExceededException_:
    out: SubscriptionLimitExceededException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class SubscriptionLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sns#SubscriptionLimitExceededException``."""

    code: str | None = "SubscriptionLimitExceededException"

    def __init__(self, data: SubscriptionLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SubscriptionLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "SubscriptionLimitExceededException":
        return cls(deserialize_query(el))
