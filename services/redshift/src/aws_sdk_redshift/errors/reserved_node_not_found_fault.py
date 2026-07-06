"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class ReservedNodeNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ReservedNodeNotFoundFault_:
    out: ReservedNodeNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ReservedNodeNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#ReservedNodeNotFoundFault``."""

    code: str | None = "ReservedNodeNotFoundFault"

    def __init__(self, data: ReservedNodeNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReservedNodeNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ReservedNodeNotFoundFault":
        return cls(deserialize_query(el))
