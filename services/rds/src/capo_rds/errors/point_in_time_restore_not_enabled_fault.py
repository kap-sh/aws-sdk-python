"""Generated from Smithy shape ``com.amazonaws.rds#PointInTimeRestoreNotEnabledFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds.types.exception_message


class PointInTimeRestoreNotEnabledFault_(TypedDict, closed=True):
    message: NotRequired["capo_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: PointInTimeRestoreNotEnabledFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> PointInTimeRestoreNotEnabledFault_:
    out: PointInTimeRestoreNotEnabledFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class PointInTimeRestoreNotEnabledFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#PointInTimeRestoreNotEnabledFault``."""

    code: str | None = "PointInTimeRestoreNotEnabledFault"

    def __init__(self, data: PointInTimeRestoreNotEnabledFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PointInTimeRestoreNotEnabledFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "PointInTimeRestoreNotEnabledFault":
        return cls(deserialize_query(el))
