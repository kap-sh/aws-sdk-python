"""Generated from Smithy shape ``com.amazonaws.ecr#TemplateNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class TemplateNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TemplateNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TemplateNotFoundException_:
    out: TemplateNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TemplateNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#TemplateNotFoundException``."""

    code: str | None = "TemplateNotFoundException"

    def __init__(self, data: TemplateNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TemplateNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TemplateNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
