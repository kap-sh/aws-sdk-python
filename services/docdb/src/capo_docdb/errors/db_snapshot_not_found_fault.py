"""Generated from Smithy shape ``com.amazonaws.docdb#DBSnapshotNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element
from capo_docdb.errors import ServiceError

if TYPE_CHECKING:
    import capo_docdb.types.exception_message


class DBSnapshotNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_docdb.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBSnapshotNotFoundFault_:
    out: DBSnapshotNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBSnapshotNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.docdb#DBSnapshotNotFoundFault``."""

    code: str | None = "DBSnapshotNotFoundFault"

    def __init__(self, data: DBSnapshotNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBSnapshotNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBSnapshotNotFoundFault":
        return cls(deserialize_query(el))
