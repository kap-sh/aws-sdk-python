"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune_graph.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.conflict_exception_reason


class ConflictException_(TypedDict):
    message: "str"
    """<p>A message describing the problem.</p>"""
    reason: NotRequired[
        "aws_sdk_neptune_graph.types.conflict_exception_reason.ConflictExceptionReason"
    ]
    """<p>The reason for the conflict exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        import aws_sdk_neptune_graph.types.conflict_exception_reason

        out["reason"] = (
            aws_sdk_neptune_graph.types.conflict_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "reason" in data:
        import aws_sdk_neptune_graph.types.conflict_exception_reason

        out["reason"] = (
            aws_sdk_neptune_graph.types.conflict_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunegraph#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
