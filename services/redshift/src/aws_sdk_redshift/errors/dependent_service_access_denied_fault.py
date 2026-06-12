"""Generated from Smithy shape ``com.amazonaws.redshift#DependentServiceAccessDeniedFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class DependentServiceAccessDeniedFault_(TypedDict):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DependentServiceAccessDeniedFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DependentServiceAccessDeniedFault_:
    out: DependentServiceAccessDeniedFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DependentServiceAccessDeniedFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#DependentServiceAccessDeniedFault``."""

    code: str | None = "DependentServiceAccessDeniedFault"

    def __init__(self, data: DependentServiceAccessDeniedFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DependentServiceAccessDeniedFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DependentServiceAccessDeniedFault":
        return cls(deserialize_query(el))
