"""Generated from Smithy shape ``com.amazonaws.cloudformation#CFNRegistryException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.error_message


class CFNRegistryException_(TypedDict):
    message: NotRequired["aws_sdk_cloudformation.types.error_message.ErrorMessage"]
    """<p>A message with details about the error that occurred.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CFNRegistryException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> CFNRegistryException_:
    out: CFNRegistryException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CFNRegistryException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#CFNRegistryException``."""

    code: str | None = "CFNRegistryException"

    def __init__(self, data: CFNRegistryException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CFNRegistryException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CFNRegistryException":
        return cls(deserialize_query(el))
