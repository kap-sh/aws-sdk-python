"""Generated from Smithy shape ``com.amazonaws.sso#UnauthorizedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso.types.error_description


class UnauthorizedException_(TypedDict, closed=True):
    message: NotRequired["capo_sso.types.error_description.ErrorDescription"]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedException_:
    out: UnauthorizedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnauthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sso#UnauthorizedException``."""

    code: str | None = "UnauthorizedException"

    def __init__(self, data: UnauthorizedException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "UnauthorizedException":
        return cls(deserialize_json(data), message)
