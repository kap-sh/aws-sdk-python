"""Generated from Smithy shape ``com.amazonaws.iam#InvalidInputException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.invalid_input_message


class InvalidInputException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_iam.types.invalid_input_message.invalidInputMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidInputException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidInputException_:
    out: InvalidInputException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidInputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#InvalidInputException``."""

    code: str | None = "InvalidInputException"

    def __init__(self, data: InvalidInputException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidInputException":
        return cls(deserialize_query(el))
