"""Generated from Smithy shape ``com.amazonaws.iam#DeleteConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.delete_conflict_message


class DeleteConflictException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.delete_conflict_message.deleteConflictMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteConflictException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DeleteConflictException_:
    out: DeleteConflictException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DeleteConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#DeleteConflictException``."""

    code: str | None = "DeleteConflictException"

    def __init__(self, data: DeleteConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeleteConflictException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DeleteConflictException":
        return cls(deserialize_query(el))
