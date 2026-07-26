"""Generated from Smithy shape ``com.amazonaws.inspector#InternalException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_inspector.types.bool
    import capo_inspector.types.error_message


class InternalException_(TypedDict, closed=True):
    message: "capo_inspector.types.error_message.ErrorMessage"
    """<p>Details of the exception error.</p>"""
    can_retry: "capo_inspector.types.bool.Bool"
    """<p>You can immediately retry your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["canRetry"] = value["can_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalException_:
    out: InternalException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalException_.message required")
    if "canRetry" in data:
        out["can_retry"] = data["canRetry"]
    else:
        raise DeserializationError("InternalException_.can_retry required")
    return out


class InternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#InternalException``."""

    code: str | None = "InternalException"

    def __init__(self, data: InternalException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalException":
        return cls(deserialize_aws_json_1_1(data))
