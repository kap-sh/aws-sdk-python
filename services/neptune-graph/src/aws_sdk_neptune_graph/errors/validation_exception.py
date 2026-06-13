"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune_graph.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: "str"
    """<p>A message describing the problem.</p>"""
    reason: NotRequired[
        "aws_sdk_neptune_graph.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason that the resource could not be validated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        import aws_sdk_neptune_graph.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_neptune_graph.types.validation_exception_reason.serialize_json(
                value["reason"]
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
        import aws_sdk_neptune_graph.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_neptune_graph.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunegraph#ValidationException``."""

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
