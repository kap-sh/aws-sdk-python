"""Generated from Smithy shape ``com.amazonaws.neptune#DomainNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element
from aws_sdk_neptune.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_neptune.types.exception_message


class DomainNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_neptune.types.exception_message.ExceptionMessage"]
    """<p>A message describing the details of the problem.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DomainNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DomainNotFoundFault_:
    out: DomainNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DomainNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptune#DomainNotFoundFault``."""

    code: str | None = "DomainNotFoundFault"

    def __init__(self, data: DomainNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DomainNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DomainNotFoundFault":
        return cls(deserialize_query(el))
