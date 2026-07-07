"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotTenantDatabaseNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class DBSnapshotTenantDatabaseNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotTenantDatabaseNotFoundFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBSnapshotTenantDatabaseNotFoundFault_:
    out: DBSnapshotTenantDatabaseNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBSnapshotTenantDatabaseNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#DBSnapshotTenantDatabaseNotFoundFault``."""

    code: str | None = "DBSnapshotTenantDatabaseNotFoundFault"

    def __init__(self, data: DBSnapshotTenantDatabaseNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBSnapshotTenantDatabaseNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBSnapshotTenantDatabaseNotFoundFault":
        return cls(deserialize_query(el))
