"""Generated from Smithy shape ``com.amazonaws.rbin#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rbin.errors import ServiceError

if TYPE_CHECKING:
    import capo_rbin.types.error_message
    import capo_rbin.types.resource_not_found_exception_reason


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_rbin.types.error_message.ErrorMessage"]
    reason: NotRequired[
        "capo_rbin.types.resource_not_found_exception_reason.ResourceNotFoundExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_rbin.types.resource_not_found_exception_reason

        out["Reason"] = (
            capo_rbin.types.resource_not_found_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import capo_rbin.types.resource_not_found_exception_reason

        out["reason"] = (
            capo_rbin.types.resource_not_found_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rbin#ResourceNotFoundException``."""

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
