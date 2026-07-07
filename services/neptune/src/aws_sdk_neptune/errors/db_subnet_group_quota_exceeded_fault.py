"""Generated from Smithy shape ``com.amazonaws.neptune#DBSubnetGroupQuotaExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element
from aws_sdk_neptune.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_neptune.types.exception_message


class DBSubnetGroupQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_neptune.types.exception_message.ExceptionMessage"]
    """<p>A message describing the details of the problem.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroupQuotaExceededFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBSubnetGroupQuotaExceededFault_:
    out: DBSubnetGroupQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBSubnetGroupQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptune#DBSubnetGroupQuotaExceededFault``."""

    code: str | None = "DBSubnetGroupQuotaExceededFault"

    def __init__(self, data: DBSubnetGroupQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBSubnetGroupQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBSubnetGroupQuotaExceededFault":
        return cls(deserialize_query(el))
