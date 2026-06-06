"""Generated from Smithy shape ``com.amazonaws.iam#UnmodifiableEntityException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.unmodifiable_entity_message


class UnmodifiableEntityException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.unmodifiable_entity_message.unmodifiableEntityMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: UnmodifiableEntityException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> UnmodifiableEntityException_:
    out: UnmodifiableEntityException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class UnmodifiableEntityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#UnmodifiableEntityException``."""

    code: str | None = "UnmodifiableEntityException"

    def __init__(self, data: UnmodifiableEntityException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnmodifiableEntityException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "UnmodifiableEntityException":
        return cls(deserialize_query(el))
