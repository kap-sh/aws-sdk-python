"""Generated from Smithy shape ``com.amazonaws.rds#InsufficientAvailableIPsInSubnetFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds.types.exception_message


class InsufficientAvailableIPsInSubnetFault_(TypedDict, closed=True):
    message: NotRequired["capo_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InsufficientAvailableIPsInSubnetFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InsufficientAvailableIPsInSubnetFault_:
    out: InsufficientAvailableIPsInSubnetFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InsufficientAvailableIPsInSubnetFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InsufficientAvailableIPsInSubnetFault``."""

    code: str | None = "InsufficientAvailableIPsInSubnetFault"

    def __init__(self, data: InsufficientAvailableIPsInSubnetFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientAvailableIPsInSubnetFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InsufficientAvailableIPsInSubnetFault":
        return cls(deserialize_query(el))
