"""Generated from Smithy shape ``com.amazonaws.elasticache#ServerlessCacheSnapshotQuotaExceededFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.exception_message


class ServerlessCacheSnapshotQuotaExceededFault_(TypedDict):
    message: NotRequired["aws_sdk_elasticache.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessCacheSnapshotQuotaExceededFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ServerlessCacheSnapshotQuotaExceededFault_:
    out: ServerlessCacheSnapshotQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ServerlessCacheSnapshotQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#ServerlessCacheSnapshotQuotaExceededFault``."""

    code: str | None = "ServerlessCacheSnapshotQuotaExceededFault"

    def __init__(self, data: ServerlessCacheSnapshotQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerlessCacheSnapshotQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ServerlessCacheSnapshotQuotaExceededFault":
        return cls(deserialize_query(el))
