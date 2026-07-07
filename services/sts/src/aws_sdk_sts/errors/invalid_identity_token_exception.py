"""Generated from Smithy shape ``com.amazonaws.sts#InvalidIdentityTokenException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sts._protocol.xml import Element
from aws_sdk_sts.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sts.types.invalid_identity_token_message


class InvalidIdentityTokenException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_sts.types.invalid_identity_token_message.invalidIdentityTokenMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidIdentityTokenException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidIdentityTokenException_:
    out: InvalidIdentityTokenException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidIdentityTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#InvalidIdentityTokenException``."""

    code: str | None = "InvalidIdentityTokenException"

    def __init__(self, data: InvalidIdentityTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidIdentityTokenException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidIdentityTokenException":
        return cls(deserialize_query(el))
