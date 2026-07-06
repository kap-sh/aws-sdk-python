"""Generated from Smithy shape ``com.amazonaws.sns#AuthorizationErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class AuthorizationErrorException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sns.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizationErrorException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> AuthorizationErrorException_:
    out: AuthorizationErrorException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class AuthorizationErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sns#AuthorizationErrorException``."""

    code: str | None = "AuthorizationErrorException"

    def __init__(self, data: AuthorizationErrorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AuthorizationErrorException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "AuthorizationErrorException":
        return cls(deserialize_query(el))
