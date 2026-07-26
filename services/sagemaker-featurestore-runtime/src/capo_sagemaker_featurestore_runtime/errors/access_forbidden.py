"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#AccessForbidden``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_featurestore_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.message


class AccessForbidden_(TypedDict, closed=True):
    message: NotRequired["capo_sagemaker_featurestore_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessForbidden_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessForbidden_:
    out: AccessForbidden_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AccessForbidden(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#AccessForbidden``."""

    code: str | None = "AccessForbidden"

    def __init__(self, data: AccessForbidden_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessForbidden",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessForbidden":
        return cls(deserialize_json(data))
