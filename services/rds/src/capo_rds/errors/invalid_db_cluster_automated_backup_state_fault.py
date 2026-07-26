"""Generated from Smithy shape ``com.amazonaws.rds#InvalidDBClusterAutomatedBackupStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds.types.exception_message


class InvalidDBClusterAutomatedBackupStateFault_(TypedDict, closed=True):
    message: NotRequired["capo_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidDBClusterAutomatedBackupStateFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidDBClusterAutomatedBackupStateFault_:
    out: InvalidDBClusterAutomatedBackupStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidDBClusterAutomatedBackupStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InvalidDBClusterAutomatedBackupStateFault``."""

    code: str | None = "InvalidDBClusterAutomatedBackupStateFault"

    def __init__(self, data: InvalidDBClusterAutomatedBackupStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDBClusterAutomatedBackupStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidDBClusterAutomatedBackupStateFault":
        return cls(deserialize_query(el))
