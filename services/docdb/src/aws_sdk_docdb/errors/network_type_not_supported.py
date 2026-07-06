"""Generated from Smithy shape ``com.amazonaws.docdb#NetworkTypeNotSupported``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element
from aws_sdk_docdb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_docdb.types.exception_message


class NetworkTypeNotSupported_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_docdb.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: NetworkTypeNotSupported_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> NetworkTypeNotSupported_:
    out: NetworkTypeNotSupported_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class NetworkTypeNotSupported(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.docdb#NetworkTypeNotSupported``."""

    code: str | None = "NetworkTypeNotSupported"

    def __init__(self, data: NetworkTypeNotSupported_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NetworkTypeNotSupported",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "NetworkTypeNotSupported":
        return cls(deserialize_query(el))
