"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionQuotaExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class ScheduledActionQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledActionQuotaExceededFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ScheduledActionQuotaExceededFault_:
    out: ScheduledActionQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ScheduledActionQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#ScheduledActionQuotaExceededFault``."""

    code: str | None = "ScheduledActionQuotaExceededFault"

    def __init__(self, data: ScheduledActionQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ScheduledActionQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ScheduledActionQuotaExceededFault":
        return cls(deserialize_query(el))
