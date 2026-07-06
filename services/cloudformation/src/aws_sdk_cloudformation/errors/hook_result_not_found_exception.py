"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookResultNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.error_message


class HookResultNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudformation.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: HookResultNotFoundException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> HookResultNotFoundException_:
    out: HookResultNotFoundException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class HookResultNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#HookResultNotFoundException``."""

    code: str | None = "HookResultNotFoundException"

    def __init__(self, data: HookResultNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="HookResultNotFoundException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "HookResultNotFoundException":
        return cls(deserialize_query(el))
