"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSnapshotNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class ClusterSnapshotNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSnapshotNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ClusterSnapshotNotFoundFault_:
    out: ClusterSnapshotNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ClusterSnapshotNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#ClusterSnapshotNotFoundFault``."""

    code: str | None = "ClusterSnapshotNotFoundFault"

    def __init__(self, data: ClusterSnapshotNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClusterSnapshotNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ClusterSnapshotNotFoundFault":
        return cls(deserialize_query(el))
