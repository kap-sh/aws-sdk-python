"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotScheduleQuotaExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift.types.exception_message


class SnapshotScheduleQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired["capo_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotScheduleQuotaExceededFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> SnapshotScheduleQuotaExceededFault_:
    out: SnapshotScheduleQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class SnapshotScheduleQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#SnapshotScheduleQuotaExceededFault``."""

    code: str | None = "SnapshotScheduleQuotaExceededFault"

    def __init__(self, data: SnapshotScheduleQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SnapshotScheduleQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "SnapshotScheduleQuotaExceededFault":
        return cls(deserialize_query(el))
