"""Generated from Smithy shape ``com.amazonaws.glacier#PolicyEnforcedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glacier.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class PolicyEnforcedException_(TypedDict, closed=True):
    type: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Client</p>"""
    code: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>PolicyEnforcedException</p>"""
    message: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>InitiateJob request denied by current data retrieval policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEnforcedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicyEnforcedException_:
    out: PolicyEnforcedException_ = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PolicyEnforcedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#PolicyEnforcedException``."""

    code: str | None = "PolicyEnforcedException"

    def __init__(self, data: PolicyEnforcedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyEnforcedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PolicyEnforcedException":
        return cls(deserialize_json(data))
