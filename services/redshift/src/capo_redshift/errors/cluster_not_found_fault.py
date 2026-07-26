"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift.types.exception_message


class ClusterNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ClusterNotFoundFault_:
    out: ClusterNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ClusterNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#ClusterNotFoundFault``."""

    code: str | None = "ClusterNotFoundFault"

    def __init__(self, data: ClusterNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClusterNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ClusterNotFoundFault":
        return cls(deserialize_query(el))
