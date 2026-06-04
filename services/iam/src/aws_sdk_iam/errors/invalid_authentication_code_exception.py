"""Generated from Smithy shape ``com.amazonaws.iam#InvalidAuthenticationCodeException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.invalid_authentication_code_message


class InvalidAuthenticationCodeException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.invalid_authentication_code_message.invalidAuthenticationCodeMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidAuthenticationCodeException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidAuthenticationCodeException_:
    out: InvalidAuthenticationCodeException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidAuthenticationCodeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#InvalidAuthenticationCodeException``."""

    code: str | None = "InvalidAuthenticationCodeException"

    def __init__(self, data: InvalidAuthenticationCodeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAuthenticationCodeException",
        )
        self.data = data
