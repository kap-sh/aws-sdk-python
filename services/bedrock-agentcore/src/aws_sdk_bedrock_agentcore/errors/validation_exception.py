"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_agentcore.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.validation_exception_field_list
    import aws_sdk_bedrock_agentcore.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: "str"
    reason: "aws_sdk_bedrock_agentcore.types.validation_exception_reason.ValidationExceptionReason"
    field_list: NotRequired[
        "aws_sdk_bedrock_agentcore.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_bedrock_agentcore.types.validation_exception_reason

    out["reason"] = (
        aws_sdk_bedrock_agentcore.types.validation_exception_reason.serialize_json(
            value["reason"]
        )
    )
    if "field_list" in value:
        import aws_sdk_bedrock_agentcore.types.validation_exception_field_list

        out["fieldList"] = (
            aws_sdk_bedrock_agentcore.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "reason" in data:
        import aws_sdk_bedrock_agentcore.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_bedrock_agentcore.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if "fieldList" in data:
        import aws_sdk_bedrock_agentcore.types.validation_exception_field_list

        out["field_list"] = (
            aws_sdk_bedrock_agentcore.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ValidationException":
        return cls(deserialize_json(data))


def serialize_event_json(value: ValidationException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "validationException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ValidationException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    return out
