"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterSnapshotNotFoundFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class DBClusterSnapshotNotFoundFault_(TypedDict):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterSnapshotNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBClusterSnapshotNotFoundFault_:
    out: DBClusterSnapshotNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBClusterSnapshotNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#DBClusterSnapshotNotFoundFault``."""

    code: str | None = "DBClusterSnapshotNotFoundFault"

    def __init__(self, data: DBClusterSnapshotNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBClusterSnapshotNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBClusterSnapshotNotFoundFault":
        return cls(deserialize_query(el))
