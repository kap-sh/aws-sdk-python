"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#AccessDeniedException``."""

from typing_extensions import TypedDict

from aws_sdk_workspaces_instances.errors import DeserializationError, ServiceError


class AccessDeniedException_(TypedDict, closed=True):
    message: "str"
    """<p>Detailed explanation of the access denial.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesinstances#AccessDeniedException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_0(data))
