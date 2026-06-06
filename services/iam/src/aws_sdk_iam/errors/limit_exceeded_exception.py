"""Generated from Smithy shape ``com.amazonaws.iam#LimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.limit_exceeded_message


class LimitExceededException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.limit_exceeded_message.limitExceededMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: LimitExceededException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "LimitExceededException":
        return cls(deserialize_query(el))
