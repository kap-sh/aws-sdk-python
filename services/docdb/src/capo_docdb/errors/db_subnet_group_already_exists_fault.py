"""Generated from Smithy shape ``com.amazonaws.docdb#DBSubnetGroupAlreadyExistsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element
from capo_docdb.errors import ServiceError

if TYPE_CHECKING:
    import capo_docdb.types.exception_message


class DBSubnetGroupAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["capo_docdb.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroupAlreadyExistsFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBSubnetGroupAlreadyExistsFault_:
    out: DBSubnetGroupAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBSubnetGroupAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.docdb#DBSubnetGroupAlreadyExistsFault``."""

    code: str | None = "DBSubnetGroupAlreadyExistsFault"

    def __init__(self, data: DBSubnetGroupAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBSubnetGroupAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBSubnetGroupAlreadyExistsFault":
        return cls(deserialize_query(el))
