"""Generated from Smithy shape ``com.amazonaws.rds#InvalidIntegrationStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class InvalidIntegrationStateFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidIntegrationStateFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidIntegrationStateFault_:
    out: InvalidIntegrationStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidIntegrationStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InvalidIntegrationStateFault``."""

    code: str | None = "InvalidIntegrationStateFault"

    def __init__(self, data: InvalidIntegrationStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidIntegrationStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidIntegrationStateFault":
        return cls(deserialize_query(el))
