"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#AccessDeniedException``."""

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_channel.errors import DeserializationError, ServiceError


class AccessDeniedException_(TypedDict, closed=True):
    message: "str"
    """<p>A message describing the access denial.</p>"""
    reason: NotRequired["str"]
    """<p>The reason for the access denial.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    if "reason" in data:
        out["reason"] = data["reason"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralchannel#AccessDeniedException``."""

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
