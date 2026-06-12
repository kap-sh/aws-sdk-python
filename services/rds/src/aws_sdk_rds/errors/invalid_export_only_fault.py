"""Generated from Smithy shape ``com.amazonaws.rds#InvalidExportOnlyFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class InvalidExportOnlyFault_(TypedDict):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidExportOnlyFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidExportOnlyFault_:
    out: InvalidExportOnlyFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidExportOnlyFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InvalidExportOnlyFault``."""

    code: str | None = "InvalidExportOnlyFault"

    def __init__(self, data: InvalidExportOnlyFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidExportOnlyFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidExportOnlyFault":
        return cls(deserialize_query(el))
