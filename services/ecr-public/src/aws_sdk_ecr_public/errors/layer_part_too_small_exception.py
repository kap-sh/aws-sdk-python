"""Generated from Smithy shape ``com.amazonaws.ecrpublic#LayerPartTooSmallException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr_public.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.exception_message


class LayerPartTooSmallException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ecr_public.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerPartTooSmallException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LayerPartTooSmallException_:
    out: LayerPartTooSmallException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class LayerPartTooSmallException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecrpublic#LayerPartTooSmallException``."""

    code: str | None = "LayerPartTooSmallException"

    def __init__(self, data: LayerPartTooSmallException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LayerPartTooSmallException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "LayerPartTooSmallException":
        return cls(deserialize_aws_json_1_1(data))
