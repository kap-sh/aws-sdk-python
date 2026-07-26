"""Generated from Smithy shape ``com.amazonaws.rds#DBUpgradeDependencyFailureFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds.types.exception_message


class DBUpgradeDependencyFailureFault_(TypedDict, closed=True):
    message: NotRequired["capo_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBUpgradeDependencyFailureFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBUpgradeDependencyFailureFault_:
    out: DBUpgradeDependencyFailureFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBUpgradeDependencyFailureFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#DBUpgradeDependencyFailureFault``."""

    code: str | None = "DBUpgradeDependencyFailureFault"

    def __init__(self, data: DBUpgradeDependencyFailureFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBUpgradeDependencyFailureFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBUpgradeDependencyFailureFault":
        return cls(deserialize_query(el))
