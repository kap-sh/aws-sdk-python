"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterEndpointAlreadyExistsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class DBClusterEndpointAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterEndpointAlreadyExistsFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBClusterEndpointAlreadyExistsFault_:
    out: DBClusterEndpointAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBClusterEndpointAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#DBClusterEndpointAlreadyExistsFault``."""

    code: str | None = "DBClusterEndpointAlreadyExistsFault"

    def __init__(self, data: DBClusterEndpointAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBClusterEndpointAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBClusterEndpointAlreadyExistsFault":
        return cls(deserialize_query(el))
