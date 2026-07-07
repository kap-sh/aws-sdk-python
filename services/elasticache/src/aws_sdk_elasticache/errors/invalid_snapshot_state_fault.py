"""Generated from Smithy shape ``com.amazonaws.elasticache#InvalidSnapshotStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.exception_message


class InvalidSnapshotStateFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_elasticache.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidSnapshotStateFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidSnapshotStateFault_:
    out: InvalidSnapshotStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidSnapshotStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#InvalidSnapshotStateFault``."""

    code: str | None = "InvalidSnapshotStateFault"

    def __init__(self, data: InvalidSnapshotStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSnapshotStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidSnapshotStateFault":
        return cls(deserialize_query(el))
