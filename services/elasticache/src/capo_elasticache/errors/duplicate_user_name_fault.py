"""Generated from Smithy shape ``com.amazonaws.elasticache#DuplicateUserNameFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element
from capo_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import capo_elasticache.types.exception_message


class DuplicateUserNameFault_(TypedDict, closed=True):
    message: NotRequired["capo_elasticache.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DuplicateUserNameFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DuplicateUserNameFault_:
    out: DuplicateUserNameFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DuplicateUserNameFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#DuplicateUserNameFault``."""

    code: str | None = "DuplicateUserNameFault"

    def __init__(self, data: DuplicateUserNameFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateUserNameFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DuplicateUserNameFault":
        return cls(deserialize_query(el))
