"""Generated from Smithy shape ``com.amazonaws.neptune#ResourceNotFoundFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element
from aws_sdk_neptune.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_neptune.types.exception_message


class ResourceNotFoundFault_(TypedDict):
    message: NotRequired["aws_sdk_neptune.types.exception_message.ExceptionMessage"]
    """<p>A message describing the details of the problem.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ResourceNotFoundFault_:
    out: ResourceNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ResourceNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptune#ResourceNotFoundFault``."""

    code: str | None = "ResourceNotFoundFault"

    def __init__(self, data: ResourceNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ResourceNotFoundFault":
        return cls(deserialize_query(el))
