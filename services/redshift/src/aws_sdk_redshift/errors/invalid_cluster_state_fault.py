"""Generated from Smithy shape ``com.amazonaws.redshift#InvalidClusterStateFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class InvalidClusterStateFault_(TypedDict):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidClusterStateFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidClusterStateFault_:
    out: InvalidClusterStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidClusterStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#InvalidClusterStateFault``."""

    code: str | None = "InvalidClusterStateFault"

    def __init__(self, data: InvalidClusterStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidClusterStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidClusterStateFault":
        return cls(deserialize_query(el))
