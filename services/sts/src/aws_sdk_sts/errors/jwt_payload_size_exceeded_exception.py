"""Generated from Smithy shape ``com.amazonaws.sts#JWTPayloadSizeExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sts._protocol.xml import Element
from aws_sdk_sts.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sts.types.jwt_payload_size_exceeded_exception2


class JWTPayloadSizeExceededException_(TypedDict):
    message: NotRequired[
        "aws_sdk_sts.types.jwt_payload_size_exceeded_exception2.JWTPayloadSizeExceededException2"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: JWTPayloadSizeExceededException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> JWTPayloadSizeExceededException_:
    out: JWTPayloadSizeExceededException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class JWTPayloadSizeExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#JWTPayloadSizeExceededException``."""

    code: str | None = "JWTPayloadSizeExceededException"

    def __init__(self, data: JWTPayloadSizeExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="JWTPayloadSizeExceededException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "JWTPayloadSizeExceededException":
        return cls(deserialize_query(el))
