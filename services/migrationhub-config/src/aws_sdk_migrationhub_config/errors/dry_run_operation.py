"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#DryRunOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhub_config.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.error_message


class DryRunOperation_(TypedDict):
    message: NotRequired["aws_sdk_migrationhub_config.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DryRunOperation_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DryRunOperation_:
    out: DryRunOperation_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DryRunOperation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubconfig#DryRunOperation``."""

    code: str | None = "DryRunOperation"

    def __init__(self, data: DryRunOperation_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DryRunOperation",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DryRunOperation":
        return cls(deserialize_aws_json_1_1(data))
