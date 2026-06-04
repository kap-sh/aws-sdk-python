"""Generated from Smithy shape ``com.amazonaws.iam#InvalidUserTypeException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.invalid_user_type_message


class InvalidUserTypeException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.invalid_user_type_message.invalidUserTypeMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidUserTypeException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidUserTypeException_:
    out: InvalidUserTypeException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidUserTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#InvalidUserTypeException``."""

    code: str | None = "InvalidUserTypeException"

    def __init__(self, data: InvalidUserTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidUserTypeException",
        )
        self.data = data
