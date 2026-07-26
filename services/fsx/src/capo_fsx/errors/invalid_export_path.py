"""Generated from Smithy shape ``com.amazonaws.fsx#InvalidExportPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class InvalidExportPath_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidExportPath_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidExportPath_:
    out: InvalidExportPath_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidExportPath(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#InvalidExportPath``."""

    code: str | None = "InvalidExportPath"

    def __init__(self, data: InvalidExportPath_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidExportPath",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidExportPath":
        return cls(deserialize_aws_json_1_1(data))
