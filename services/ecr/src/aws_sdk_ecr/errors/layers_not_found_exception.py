"""Generated from Smithy shape ``com.amazonaws.ecr#LayersNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class LayersNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]
    """<p>The error message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayersNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LayersNotFoundException_:
    out: LayersNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class LayersNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#LayersNotFoundException``."""

    code: str | None = "LayersNotFoundException"

    def __init__(self, data: LayersNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LayersNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "LayersNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
