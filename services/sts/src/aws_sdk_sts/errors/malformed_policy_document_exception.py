"""Generated from Smithy shape ``com.amazonaws.sts#MalformedPolicyDocumentException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sts._protocol.xml import Element
from aws_sdk_sts.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sts.types.malformed_policy_document_message


class MalformedPolicyDocumentException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_sts.types.malformed_policy_document_message.malformedPolicyDocumentMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: MalformedPolicyDocumentException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> MalformedPolicyDocumentException_:
    out: MalformedPolicyDocumentException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class MalformedPolicyDocumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#MalformedPolicyDocumentException``."""

    code: str | None = "MalformedPolicyDocumentException"

    def __init__(self, data: MalformedPolicyDocumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedPolicyDocumentException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "MalformedPolicyDocumentException":
        return cls(deserialize_query(el))
