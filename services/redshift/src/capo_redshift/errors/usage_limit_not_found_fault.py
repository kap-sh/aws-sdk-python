"""Generated from Smithy shape ``com.amazonaws.redshift#UsageLimitNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift.types.exception_message


class UsageLimitNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: UsageLimitNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> UsageLimitNotFoundFault_:
    out: UsageLimitNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class UsageLimitNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#UsageLimitNotFoundFault``."""

    code: str | None = "UsageLimitNotFoundFault"

    def __init__(self, data: UsageLimitNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UsageLimitNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "UsageLimitNotFoundFault":
        return cls(deserialize_query(el))
