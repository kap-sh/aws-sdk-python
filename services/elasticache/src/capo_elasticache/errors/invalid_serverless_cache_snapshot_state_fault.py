"""Generated from Smithy shape ``com.amazonaws.elasticache#InvalidServerlessCacheSnapshotStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element
from capo_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import capo_elasticache.types.exception_message


class InvalidServerlessCacheSnapshotStateFault_(TypedDict, closed=True):
    message: NotRequired["capo_elasticache.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidServerlessCacheSnapshotStateFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidServerlessCacheSnapshotStateFault_:
    out: InvalidServerlessCacheSnapshotStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidServerlessCacheSnapshotStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#InvalidServerlessCacheSnapshotStateFault``."""

    code: str | None = "InvalidServerlessCacheSnapshotStateFault"

    def __init__(self, data: InvalidServerlessCacheSnapshotStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidServerlessCacheSnapshotStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidServerlessCacheSnapshotStateFault":
        return cls(deserialize_query(el))
