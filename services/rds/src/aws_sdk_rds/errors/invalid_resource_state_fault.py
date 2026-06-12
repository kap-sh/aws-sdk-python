"""Generated from Smithy shape ``com.amazonaws.rds#InvalidResourceStateFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class InvalidResourceStateFault_(TypedDict):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidResourceStateFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidResourceStateFault_:
    out: InvalidResourceStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidResourceStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InvalidResourceStateFault``."""

    code: str | None = "InvalidResourceStateFault"

    def __init__(self, data: InvalidResourceStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidResourceStateFault":
        return cls(deserialize_query(el))
