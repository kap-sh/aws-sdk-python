"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DisabledOperationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticsearch_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.error_message


class DisabledOperationException_(TypedDict):
    message: NotRequired[
        "aws_sdk_elasticsearch_service.types.error_message.ErrorMessage"
    ]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisabledOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DisabledOperationException_:
    out: DisabledOperationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DisabledOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticsearchservice#DisabledOperationException``."""

    code: str | None = "DisabledOperationException"

    def __init__(self, data: DisabledOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DisabledOperationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DisabledOperationException":
        return cls(deserialize_json(data))
