"""Generated from Smithy shape ``com.amazonaws.redshift#DependentServiceUnavailableFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class DependentServiceUnavailableFault_(TypedDict):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DependentServiceUnavailableFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DependentServiceUnavailableFault_:
    out: DependentServiceUnavailableFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DependentServiceUnavailableFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#DependentServiceUnavailableFault``."""

    code: str | None = "DependentServiceUnavailableFault"

    def __init__(self, data: DependentServiceUnavailableFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DependentServiceUnavailableFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DependentServiceUnavailableFault":
        return cls(deserialize_query(el))
