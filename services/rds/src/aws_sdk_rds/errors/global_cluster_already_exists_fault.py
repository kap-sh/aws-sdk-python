"""Generated from Smithy shape ``com.amazonaws.rds#GlobalClusterAlreadyExistsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class GlobalClusterAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClusterAlreadyExistsFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> GlobalClusterAlreadyExistsFault_:
    out: GlobalClusterAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class GlobalClusterAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#GlobalClusterAlreadyExistsFault``."""

    code: str | None = "GlobalClusterAlreadyExistsFault"

    def __init__(self, data: GlobalClusterAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GlobalClusterAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "GlobalClusterAlreadyExistsFault":
        return cls(deserialize_query(el))
