"""Generated from Smithy shape ``com.amazonaws.ses#AccountSendingPausedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ses.types.error_message


class AccountSendingPausedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountSendingPausedException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> AccountSendingPausedException_:
    out: AccountSendingPausedException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class AccountSendingPausedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#AccountSendingPausedException``."""

    code: str | None = "AccountSendingPausedException"

    def __init__(self, data: AccountSendingPausedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccountSendingPausedException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "AccountSendingPausedException":
        return cls(deserialize_query(el))
