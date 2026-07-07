"""Generated from Smithy shape ``com.amazonaws.iam#UnrecognizedPublicKeyEncodingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.unrecognized_public_key_encoding_message


class UnrecognizedPublicKeyEncodingException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_iam.types.unrecognized_public_key_encoding_message.unrecognizedPublicKeyEncodingMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: UnrecognizedPublicKeyEncodingException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> UnrecognizedPublicKeyEncodingException_:
    out: UnrecognizedPublicKeyEncodingException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class UnrecognizedPublicKeyEncodingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#UnrecognizedPublicKeyEncodingException``."""

    code: str | None = "UnrecognizedPublicKeyEncodingException"

    def __init__(self, data: UnrecognizedPublicKeyEncodingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnrecognizedPublicKeyEncodingException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "UnrecognizedPublicKeyEncodingException":
        return cls(deserialize_query(el))
