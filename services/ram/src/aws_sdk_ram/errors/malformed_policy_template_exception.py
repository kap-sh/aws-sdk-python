"""Generated from Smithy shape ``com.amazonaws.ram#MalformedPolicyTemplateException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class MalformedPolicyTemplateException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: MalformedPolicyTemplateException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MalformedPolicyTemplateException_:
    out: MalformedPolicyTemplateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("MalformedPolicyTemplateException_.message required")
    return out


class MalformedPolicyTemplateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#MalformedPolicyTemplateException``."""

    code: str | None = "MalformedPolicyTemplateException"

    def __init__(self, data: MalformedPolicyTemplateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedPolicyTemplateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MalformedPolicyTemplateException":
        return cls(deserialize_json(data))
