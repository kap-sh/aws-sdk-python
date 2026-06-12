"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#DependencyFailedException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_runtime_v2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.string


class DependencyFailedException_(TypedDict):
    message: "aws_sdk_lex_runtime_v2.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: DependencyFailedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependencyFailedException_:
    out: DependencyFailedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DependencyFailedException_.message required")
    return out


class DependencyFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimev2#DependencyFailedException``."""

    code: str | None = "DependencyFailedException"

    def __init__(self, data: DependencyFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyFailedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DependencyFailedException":
        return cls(deserialize_json(data))
