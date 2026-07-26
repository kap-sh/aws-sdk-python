"""Generated from Smithy shape ``com.amazonaws.elasticache#ServerlessCacheQuotaForCustomerExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element
from capo_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import capo_elasticache.types.exception_message


class ServerlessCacheQuotaForCustomerExceededFault_(TypedDict, closed=True):
    message: NotRequired["capo_elasticache.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessCacheQuotaForCustomerExceededFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ServerlessCacheQuotaForCustomerExceededFault_:
    out: ServerlessCacheQuotaForCustomerExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ServerlessCacheQuotaForCustomerExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#ServerlessCacheQuotaForCustomerExceededFault``."""

    code: str | None = "ServerlessCacheQuotaForCustomerExceededFault"

    def __init__(self, data: ServerlessCacheQuotaForCustomerExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerlessCacheQuotaForCustomerExceededFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ServerlessCacheQuotaForCustomerExceededFault":
        return cls(deserialize_query(el))
