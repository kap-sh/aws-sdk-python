"""Generated from Smithy shape ``com.amazonaws.novaact#AccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_nova_act.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.non_blank_string


class AccessDeniedException_(TypedDict, closed=True):
    message: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>You don't have sufficient permissions to perform this action. Verify your IAM permissions and try again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.novaact#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))
