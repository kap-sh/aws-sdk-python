"""Generated from Smithy shape ``com.amazonaws.cognitosync#InvalidLambdaFunctionOutputException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.exception_message


class InvalidLambdaFunctionOutputException_(TypedDict):
    message: "aws_sdk_cognito_sync.types.exception_message.ExceptionMessage"
    """<p>A message returned when an InvalidLambdaFunctionOutputException occurs</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidLambdaFunctionOutputException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidLambdaFunctionOutputException_:
    out: InvalidLambdaFunctionOutputException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "InvalidLambdaFunctionOutputException_.message required"
        )
    return out


class InvalidLambdaFunctionOutputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#InvalidLambdaFunctionOutputException``."""

    code: str | None = "InvalidLambdaFunctionOutputException"

    def __init__(self, data: InvalidLambdaFunctionOutputException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidLambdaFunctionOutputException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidLambdaFunctionOutputException":
        return cls(deserialize_json(data))
