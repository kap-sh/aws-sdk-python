"""Generated from Smithy shape ``com.amazonaws.iam#DuplicateSSHPublicKeyException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.duplicate_ssh_public_key_message


class DuplicateSSHPublicKeyException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.duplicate_ssh_public_key_message.duplicateSSHPublicKeyMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DuplicateSSHPublicKeyException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DuplicateSSHPublicKeyException_:
    out: DuplicateSSHPublicKeyException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DuplicateSSHPublicKeyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#DuplicateSSHPublicKeyException``."""

    code: str | None = "DuplicateSSHPublicKeyException"

    def __init__(self, data: DuplicateSSHPublicKeyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateSSHPublicKeyException",
        )
        self.data = data
