"""Generated from Smithy shape ``com.amazonaws.docdb#DBSubnetGroupNotFoundFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element
from aws_sdk_docdb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_docdb.types.exception_message


class DBSubnetGroupNotFoundFault_(TypedDict):
    message: NotRequired["aws_sdk_docdb.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroupNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBSubnetGroupNotFoundFault_:
    out: DBSubnetGroupNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBSubnetGroupNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.docdb#DBSubnetGroupNotFoundFault``."""

    code: str | None = "DBSubnetGroupNotFoundFault"

    def __init__(self, data: DBSubnetGroupNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBSubnetGroupNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBSubnetGroupNotFoundFault":
        return cls(deserialize_query(el))
