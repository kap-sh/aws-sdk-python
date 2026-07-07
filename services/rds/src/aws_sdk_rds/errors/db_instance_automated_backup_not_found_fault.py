"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceAutomatedBackupNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class DBInstanceAutomatedBackupNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceAutomatedBackupNotFoundFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBInstanceAutomatedBackupNotFoundFault_:
    out: DBInstanceAutomatedBackupNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBInstanceAutomatedBackupNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#DBInstanceAutomatedBackupNotFoundFault``."""

    code: str | None = "DBInstanceAutomatedBackupNotFoundFault"

    def __init__(self, data: DBInstanceAutomatedBackupNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBInstanceAutomatedBackupNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBInstanceAutomatedBackupNotFoundFault":
        return cls(deserialize_query(el))
