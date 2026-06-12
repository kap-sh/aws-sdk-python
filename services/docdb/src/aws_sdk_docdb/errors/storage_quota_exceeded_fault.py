"""Generated from Smithy shape ``com.amazonaws.docdb#StorageQuotaExceededFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element
from aws_sdk_docdb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_docdb.types.exception_message


class StorageQuotaExceededFault_(TypedDict):
    message: NotRequired["aws_sdk_docdb.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: StorageQuotaExceededFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> StorageQuotaExceededFault_:
    out: StorageQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class StorageQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.docdb#StorageQuotaExceededFault``."""

    code: str | None = "StorageQuotaExceededFault"

    def __init__(self, data: StorageQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="StorageQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "StorageQuotaExceededFault":
        return cls(deserialize_query(el))
