"""Generated from Smithy shape ``com.amazonaws.cloudformation#InvalidChangeSetStatusException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.error_message


class InvalidChangeSetStatusException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudformation.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidChangeSetStatusException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidChangeSetStatusException_:
    out: InvalidChangeSetStatusException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidChangeSetStatusException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#InvalidChangeSetStatusException``."""

    code: str | None = "InvalidChangeSetStatusException"

    def __init__(self, data: InvalidChangeSetStatusException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidChangeSetStatusException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidChangeSetStatusException":
        return cls(deserialize_query(el))
