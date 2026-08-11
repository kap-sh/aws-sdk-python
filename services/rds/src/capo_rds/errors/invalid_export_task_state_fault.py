"""Generated from Smithy shape ``com.amazonaws.rds#InvalidExportTaskStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds.types.exception_message


class InvalidExportTaskStateFault_(TypedDict, closed=True):
    message: NotRequired["capo_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidExportTaskStateFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidExportTaskStateFault_:
    out: InvalidExportTaskStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidExportTaskStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InvalidExportTaskStateFault``."""

    code: str | None = "InvalidExportTaskStateFault"

    def __init__(self, data: InvalidExportTaskStateFault_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidExportTaskStateFault",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None
    ) -> "InvalidExportTaskStateFault":
        return cls(deserialize_query(el), message)
