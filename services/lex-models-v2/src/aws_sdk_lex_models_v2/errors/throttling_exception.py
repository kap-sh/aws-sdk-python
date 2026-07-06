"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.exception_message
    import aws_sdk_lex_models_v2.types.retry_after_seconds


class ThrottlingException_(TypedDict, closed=True):
    retry_after_seconds: (
        "aws_sdk_lex_models_v2.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>The number of seconds after which the user can invoke the API again.</p>"""
    message: NotRequired[
        "aws_sdk_lex_models_v2.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexmodelsv2#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
