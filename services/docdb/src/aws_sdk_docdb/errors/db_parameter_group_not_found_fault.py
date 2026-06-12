"""Generated from Smithy shape ``com.amazonaws.docdb#DBParameterGroupNotFoundFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element
from aws_sdk_docdb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_docdb.types.exception_message


class DBParameterGroupNotFoundFault_(TypedDict):
    message: NotRequired["aws_sdk_docdb.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroupNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBParameterGroupNotFoundFault_:
    out: DBParameterGroupNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBParameterGroupNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.docdb#DBParameterGroupNotFoundFault``."""

    code: str | None = "DBParameterGroupNotFoundFault"

    def __init__(self, data: DBParameterGroupNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBParameterGroupNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBParameterGroupNotFoundFault":
        return cls(deserialize_query(el))
