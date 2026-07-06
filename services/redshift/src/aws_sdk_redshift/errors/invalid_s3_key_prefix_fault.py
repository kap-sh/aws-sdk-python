"""Generated from Smithy shape ``com.amazonaws.redshift#InvalidS3KeyPrefixFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class InvalidS3KeyPrefixFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidS3KeyPrefixFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidS3KeyPrefixFault_:
    out: InvalidS3KeyPrefixFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidS3KeyPrefixFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#InvalidS3KeyPrefixFault``."""

    code: str | None = "InvalidS3KeyPrefixFault"

    def __init__(self, data: InvalidS3KeyPrefixFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidS3KeyPrefixFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidS3KeyPrefixFault":
        return cls(deserialize_query(el))
