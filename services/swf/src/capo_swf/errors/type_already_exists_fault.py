"""Generated from Smithy shape ``com.amazonaws.swf#TypeAlreadyExistsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import ServiceError

if TYPE_CHECKING:
    import capo_swf.types.error_message


class TypeAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["capo_swf.types.error_message.ErrorMessage"]
    """<p>A description that may help with diagnosing the cause of the fault.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TypeAlreadyExistsFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TypeAlreadyExistsFault_:
    out: TypeAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TypeAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.swf#TypeAlreadyExistsFault``."""

    code: str | None = "TypeAlreadyExistsFault"

    def __init__(self, data: TypeAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TypeAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "TypeAlreadyExistsFault":
        return cls(deserialize_aws_json_1_0(data))
