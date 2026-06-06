"""Generated from Smithy shape ``com.amazonaws.iam#EntityTemporarilyUnmodifiableException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.entity_temporarily_unmodifiable_message


class EntityTemporarilyUnmodifiableException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.entity_temporarily_unmodifiable_message.entityTemporarilyUnmodifiableMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: EntityTemporarilyUnmodifiableException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> EntityTemporarilyUnmodifiableException_:
    out: EntityTemporarilyUnmodifiableException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class EntityTemporarilyUnmodifiableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#EntityTemporarilyUnmodifiableException``."""

    code: str | None = "EntityTemporarilyUnmodifiableException"

    def __init__(self, data: EntityTemporarilyUnmodifiableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntityTemporarilyUnmodifiableException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "EntityTemporarilyUnmodifiableException":
        return cls(deserialize_query(el))
