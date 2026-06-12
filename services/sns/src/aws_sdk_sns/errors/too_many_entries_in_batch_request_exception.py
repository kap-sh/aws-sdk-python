"""Generated from Smithy shape ``com.amazonaws.sns#TooManyEntriesInBatchRequestException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class TooManyEntriesInBatchRequestException_(TypedDict):
    message: NotRequired["aws_sdk_sns.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TooManyEntriesInBatchRequestException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> TooManyEntriesInBatchRequestException_:
    out: TooManyEntriesInBatchRequestException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyEntriesInBatchRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sns#TooManyEntriesInBatchRequestException``."""

    code: str | None = "TooManyEntriesInBatchRequestException"

    def __init__(self, data: TooManyEntriesInBatchRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyEntriesInBatchRequestException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "TooManyEntriesInBatchRequestException":
        return cls(deserialize_query(el))
