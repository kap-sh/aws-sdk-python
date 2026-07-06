"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetNotEmptyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.error_message


class StackSetNotEmptyException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudformation.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetNotEmptyException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> StackSetNotEmptyException_:
    out: StackSetNotEmptyException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class StackSetNotEmptyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#StackSetNotEmptyException``."""

    code: str | None = "StackSetNotEmptyException"

    def __init__(self, data: StackSetNotEmptyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="StackSetNotEmptyException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "StackSetNotEmptyException":
        return cls(deserialize_query(el))
