"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotCopyAlreadyDisabledFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift.types.exception_message


class SnapshotCopyAlreadyDisabledFault_(TypedDict, closed=True):
    message: NotRequired["capo_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotCopyAlreadyDisabledFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> SnapshotCopyAlreadyDisabledFault_:
    out: SnapshotCopyAlreadyDisabledFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class SnapshotCopyAlreadyDisabledFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#SnapshotCopyAlreadyDisabledFault``."""

    code: str | None = "SnapshotCopyAlreadyDisabledFault"

    def __init__(self, data: SnapshotCopyAlreadyDisabledFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SnapshotCopyAlreadyDisabledFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "SnapshotCopyAlreadyDisabledFault":
        return cls(deserialize_query(el))
