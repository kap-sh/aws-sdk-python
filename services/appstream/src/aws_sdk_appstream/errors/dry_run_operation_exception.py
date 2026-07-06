"""Generated from Smithy shape ``com.amazonaws.appstream#DryRunOperationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appstream.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appstream.types.error_message


class DryRunOperationException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appstream.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DryRunOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DryRunOperationException_:
    out: DryRunOperationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DryRunOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appstream#DryRunOperationException``."""

    code: str | None = "DryRunOperationException"

    def __init__(self, data: DryRunOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DryRunOperationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DryRunOperationException":
        return cls(deserialize_aws_json_1_1(data))
