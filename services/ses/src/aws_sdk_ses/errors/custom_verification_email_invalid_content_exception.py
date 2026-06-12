"""Generated from Smithy shape ``com.amazonaws.ses#CustomVerificationEmailInvalidContentException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ses.types.error_message


class CustomVerificationEmailInvalidContentException_(TypedDict):
    message: NotRequired["aws_sdk_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomVerificationEmailInvalidContentException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> CustomVerificationEmailInvalidContentException_:
    out: CustomVerificationEmailInvalidContentException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CustomVerificationEmailInvalidContentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#CustomVerificationEmailInvalidContentException``."""

    code: str | None = "CustomVerificationEmailInvalidContentException"

    def __init__(self, data: CustomVerificationEmailInvalidContentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomVerificationEmailInvalidContentException",
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element
    ) -> "CustomVerificationEmailInvalidContentException":
        return cls(deserialize_query(el))
