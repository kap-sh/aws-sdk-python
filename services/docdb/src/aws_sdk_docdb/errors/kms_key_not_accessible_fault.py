"""Generated from Smithy shape ``com.amazonaws.docdb#KMSKeyNotAccessibleFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element
from aws_sdk_docdb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_docdb.types.exception_message


class KMSKeyNotAccessibleFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_docdb.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: KMSKeyNotAccessibleFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> KMSKeyNotAccessibleFault_:
    out: KMSKeyNotAccessibleFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class KMSKeyNotAccessibleFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.docdb#KMSKeyNotAccessibleFault``."""

    code: str | None = "KMSKeyNotAccessibleFault"

    def __init__(self, data: KMSKeyNotAccessibleFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSKeyNotAccessibleFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "KMSKeyNotAccessibleFault":
        return cls(deserialize_query(el))
