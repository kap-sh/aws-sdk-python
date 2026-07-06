"""Generated from Smithy shape ``com.amazonaws.neptunegraph#UnprocessableException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.unprocessable_exception_reason


class UnprocessableException_(TypedDict, closed=True):
    message: "str"
    reason: "aws_sdk_neptune_graph.types.unprocessable_exception_reason.UnprocessableExceptionReason"
    """<p>The reason for the unprocessable exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_neptune_graph.types.unprocessable_exception_reason

    out["reason"] = (
        aws_sdk_neptune_graph.types.unprocessable_exception_reason.serialize_json(
            value["reason"]
        )
    )
    return out


def deserialize_json(data: dict) -> UnprocessableException_:
    out: UnprocessableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("UnprocessableException_.message required")
    if "reason" in data:
        import aws_sdk_neptune_graph.types.unprocessable_exception_reason

        out["reason"] = (
            aws_sdk_neptune_graph.types.unprocessable_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("UnprocessableException_.reason required")
    return out


class UnprocessableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunegraph#UnprocessableException``."""

    code: str | None = "UnprocessableException"

    def __init__(self, data: UnprocessableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnprocessableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnprocessableException":
        return cls(deserialize_json(data))
