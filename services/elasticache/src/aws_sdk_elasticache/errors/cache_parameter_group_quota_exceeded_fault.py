"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheParameterGroupQuotaExceededFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.exception_message


class CacheParameterGroupQuotaExceededFault_(TypedDict):
    message: NotRequired["aws_sdk_elasticache.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheParameterGroupQuotaExceededFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> CacheParameterGroupQuotaExceededFault_:
    out: CacheParameterGroupQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CacheParameterGroupQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#CacheParameterGroupQuotaExceededFault``."""

    code: str | None = "CacheParameterGroupQuotaExceededFault"

    def __init__(self, data: CacheParameterGroupQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CacheParameterGroupQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CacheParameterGroupQuotaExceededFault":
        return cls(deserialize_query(el))
