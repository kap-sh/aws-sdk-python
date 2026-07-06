"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53_recovery_readiness.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_route53_recovery_readiness.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53recoveryreadiness#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_json(data))
