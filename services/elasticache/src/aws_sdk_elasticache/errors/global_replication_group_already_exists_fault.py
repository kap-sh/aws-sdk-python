"""Generated from Smithy shape ``com.amazonaws.elasticache#GlobalReplicationGroupAlreadyExistsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.exception_message


class GlobalReplicationGroupAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_elasticache.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalReplicationGroupAlreadyExistsFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> GlobalReplicationGroupAlreadyExistsFault_:
    out: GlobalReplicationGroupAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class GlobalReplicationGroupAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#GlobalReplicationGroupAlreadyExistsFault``."""

    code: str | None = "GlobalReplicationGroupAlreadyExistsFault"

    def __init__(self, data: GlobalReplicationGroupAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GlobalReplicationGroupAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "GlobalReplicationGroupAlreadyExistsFault":
        return cls(deserialize_query(el))
