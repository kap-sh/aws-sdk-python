"""Generated from Smithy shape ``com.amazonaws.mgn#UninitializedAccountException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.large_bounded_string


class UninitializedAccountException_(TypedDict):
    message: NotRequired["aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"]
    code: NotRequired["aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"]


# --- restJson1 ser/de ---
def serialize_json(value: UninitializedAccountException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> UninitializedAccountException_:
    out: UninitializedAccountException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    return out


class UninitializedAccountException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mgn#UninitializedAccountException``."""

    code: str | None = "UninitializedAccountException"

    def __init__(self, data: UninitializedAccountException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UninitializedAccountException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UninitializedAccountException":
        return cls(deserialize_json(data))
