"""Generated from Smithy shape ``com.amazonaws.ecr#UnsupportedImageTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr.types.exception_message


class UnsupportedImageTypeException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedImageTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedImageTypeException_:
    out: UnsupportedImageTypeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedImageTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#UnsupportedImageTypeException``."""

    code: str | None = "UnsupportedImageTypeException"

    def __init__(self, data: UnsupportedImageTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedImageTypeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedImageTypeException":
        return cls(deserialize_aws_json_1_1(data))
